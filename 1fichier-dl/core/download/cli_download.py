import os
import json
import requests
import lxml
import time
from .helpers import (get_proxy, convert_size, download_speed,
                       PLATFORM, is_valid_link)

def download(url, password = None, payload={'dl_no_ssl': 'on', 'dlinline': 'on'}):
        if is_valid_link(url):
            if not 'https://' in url[0:8] and not 'http://' in url[0:7]:
                url = f'https://{url}'
            if '&' in url:
                url = url.split('&')[0]
            if '/dir/' in url:
                folder = requests.get(f'{url}?json=1')
                folder = folder.json()
                print(f'Loaded folder {url} with {len(folder)} files.')
                for f in folder:
                    download(f['link'], password)
        else:
            print(f'{url} is not a valid 1Fichier link.')
            return

        print(f'Starting download: {url}..')

        while True:
            if password: payload['pass'] = password
            proxy = get_proxy()
            proxies = {'https': proxy} if PLATFORM == 'nt' else {'https': f'https://{proxy}'}
            try:
                r = requests.post(url, payload, proxies=proxies)
                print(r.text)
                html = lxml.html.fromstring(r.content)
                if html.xpath('//*[@id="pass"]'):
                    password = input(f'Password needed for {url}: ')
                    payload['pass'] = password
            except:
                # Proxy failed.
                print(f'\rBypassing..\n', end='', flush=True)
                pass
            else:
                # Proxy worked.
                print('\rBypassed.. \n', end='', flush=True)
                break

        if not html.xpath('/html/body/div[4]/div[2]/a'):
            if 'Bad password' in r.text:
                password = input(f'(Wrong password) Password needed for {url}: ')
                payload['pass'] = password
        else:
            old_url = url
            url = html.xpath('/html/body/div[4]/div[2]/a')[0].get('href')
        
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                'Referer': old_url
            }

            r = requests.get(url, stream=True, headers=headers)

            if 'Content-Disposition' in r.headers:
                name = r.headers['Content-Disposition'].split('"')[1]

                if os.path.exists(f'{name}'):
                    i = 1
                    while os.path.exists(f'({i}) {name}'):
                        i += 1
                    name = f'({i}) {name}'

                name = f'{name}.unfinished' if name[-11:] != '.unfinished' else name

                print(f'Downloading: {name[:-11]}')

                with open(name, 'ab') as f:
                    chunk_size = 8192
                    bytes_read = 0
                    start = time.time()
                    for chunk in r.iter_content(chunk_size):
                        f.write(chunk)
                        bytes_read += len(chunk)
                        total_per = 100 * (float(bytes_read))
                        total_per /= float(r.headers['Content-Length'])
                        dl_speed = download_speed(bytes_read, start)
                        print(f'\r| {round(total_per, 1)}% | {dl_speed} '.ljust(21), end='', flush=True)
                print(f'| {round(total_per, 1)}% | Finished.'.ljust(21))
                os.rename(name, name[:-11])
                return

        download(url)
