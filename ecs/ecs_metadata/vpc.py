#!/usr/bin/python
#-* coding: utf-8 -*-

"""
Get metadata of aliyun ecs instances in vpc.

Reference:
    Instance Metadata:
        https://help.aliyun.com/knowledge_detail/49122.html
"""

import requests

metadata_url = 'http://100.100.100.200/latest/meta-data'

r = requests.get(metadata_url)

metadata = {}
metadata_key_w = 0
metadata_con_w = 0
metadata_keys = r.content

for key in metadata_keys.split('\n'):
    if '/' not in key and key != 'source-address':
        rk = requests.get('/'.join([metadata_url ,key]))
        content = rk.content.strip()
        key_len = len(key + ':')
        con_len = len(content)

        if content:
            metadata[key] = content
        else:
            metadata[key] = None

        if key_len > metadata_key_w:
            metadata_key_w = key_len
        if con_len > metadata_con_w:
            metadata_con_w = con_len

def main():
    #print metadata_key_w
    print 'Name'.center(metadata_key_w,'-'), 'Metadata'.center(metadata_con_w, '-')
    for k in metadata:
        name = k + ':'
        print name.rjust(metadata_key_w, ' '), metadata[k]
    print '-' * (metadata_key_w + metadata_con_w + 1)

if __name__ == '__main__':
    main()
