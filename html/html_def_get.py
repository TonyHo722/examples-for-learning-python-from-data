#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import makedirs
from os.path import exists, join
from hashlib import md5

import requests

def get(url, cache_dir_path='cache/'):

    if not exists(cache_dir_path):
        makedirs(cache_dir_path)

    cache_path = join(cache_dir_path, md5(url).hexdigest())
    if exists(cache_path):
        with open(cache_path) as f:
            content = f.read().decode('utf-8')
        return content
    else:
        content = requests.get(url).content
        with open(cache_path, 'w') as f:
            f.write(content)
        return content

if __name__ == '__main__':
    print get('http://clbc.tw')
