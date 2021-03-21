import requests
import math
import os
import time
import lxml.html

PROXY_TXT_API = 'https://www.proxyscan.io/api/proxy?type=https&format=txt'
PLATFORM = os.name

def get_proxy():
    '''
    Get proxy (str) from API.
    '''
    proxy = requests.get(PROXY_TXT_API).text
    return proxy.rstrip()

def convert_size(size_bytes):
    '''
    Convert from bytes to human readable sizes (str).
    '''
    # https://stackoverflow.com/a/14822210
    if size_bytes == 0:
        return '0 B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return '%s %s' % (s, size_name[i])

def download_speed(bytes_read, start_time):
    '''
    Convert speed to human readable speed (str).
    '''
    if bytes_read == 0:
        return '0 B/s'
    elif time.time()-start_time == 0:
        return '- B/s'
    size_name = ('B/s', 'KB/s', 'MB/s', 'GB/s', 'TB/s')
    bps = bytes_read/(time.time()-start_time)
    i = int(math.floor(math.log(bps, 1024)))
    p = math.pow(1024, i)
    s = round(bps / p, 2)
    return '%s %s' % (s, size_name[i])

def get_link_info(url):
    '''
    Get file name and size.
    Returns list: [File Name, Downloaded Size]
    '''
    try:
        r = requests.get(url)
        html = lxml.html.fromstring(r.content)
        if html.xpath('//*[@id="pass"]'):
            return ['Private File', '- MB']
        name = html.xpath('//td[@class=\'normal\']')[0].text
        size = html.xpath('//td[@class=\'normal\']')[2].text
        return [name, size]
    except:
        return None