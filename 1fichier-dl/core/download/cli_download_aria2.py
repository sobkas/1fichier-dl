import os
import json
import requests
import lxml
import time
import random
from .helpers import (get_proxies, convert_size, download_speed, is_valid_link)
from .pyaria2 import PyAria2
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download(url, password = None, payload={'dl_no_ssl': 'on', 'dlinline': 'on'}):
        PyAria2().__init__
        opts_dict={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36", "Referer": url}
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
            proxies = get_proxies("")
            if proxies[0] is None:
                continue
            for proxy_list in proxies:
                if proxy_list is None:
                    continue
                if proxy_list["https"] in PyAria2().proxy_black_list:
                    print("Proxy black listed: {}".format(proxy_list["https"]))
                    continue
                r = None
                try:
                    r = requests.post(url, payload, proxies=proxy_list, verify=False, timeout=20)
                    html = lxml.html.fromstring(r.content)
                    if html.xpath('//*[@id="pass"]'):
                        password = raw_input('Password needed for {url}: ')
                        payload['pass'] = password
                except:
                    # Proxy failed.
                    print(f'\rBypassing..\n', end='', flush=True)
                    print("Proxy: {}\n".format(proxy_list))
                    PyAria2().proxy_black_list.append(proxy_list["https"])
                    pass
                else:
                    if html.xpath('/html/body/div[4]/div[2]/a'):
                        new_url = html.xpath('/html/body/div[4]/div[2]/a')[0].get('href')
                    else:
                        continue
                    r = requests.head(new_url, proxies=proxy_list, headers=opts_dict, verify=False)
                    if r.headers.get("Content-Disposition") is None:
                        continue
                    else:
                        print("Succesful proxy: {}\n".format(proxy_list))
                        break
            else:
                continue
            break

        print("Bypassed,Getting link......\n")

        opts = {"header": ['User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36', 'Referer: '+url+'']}

        try:
                PyAria2().addUri([new_url], options=opts)
        except:
                print("Couldn't send Uri: {} to aria2".format(new_url))
        else:
                print("Download sent to aria2.")
        return




