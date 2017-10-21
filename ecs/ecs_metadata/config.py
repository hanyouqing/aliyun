# -*- couding: utf-8 -*-

import os
import sys
import ConfigParser
import logging
import argparse


home = os.environ.get("HOME")
aliyun_conf = os.path.join(home, '.aliyun')
aliyun_ini = os.path.join(aliyun_conf, 'config.ini')

aliyun_ecs_conf = os.path.join(aliyun_conf, 'ecs')
aliyun_ecs_ini = os.path.join(aliyun_ecs_conf, 'config.ini')
aliyun_ecs_instanceid = os.path.join(aliyun_ecs_conf, 'instanceid')
aliyun_ecs_metadata = os.path.join(aliyun_ecs_conf, 'metadata')

defaults = """
[global]
UID = Your UID

[ecs]
AccessKeyId = Your AccessKeyId 
AccessKeySecret = Your AccessKeySecret

[vpc]
URL = http://100.100.100.200/latest/meta-data

[cms]
CmsHost = open.cms.aliyun.com
CmsPort = 80
CmsMonitorUri = /metrics/put
"""

ecs_config = {}
ecs_metadata = {}



def _default(default):
    if os.path.exists(aliyun_ecs_conf) == False:
        os.makedirs(aliyun_ecs_conf)
    fp = open(aliyun_ini, "w")
    fp.write(defaults)
    fp.close()

def _config():
    if os.path.exists(aliyun_ini) == False or os.path.getsize(aliyun_ini) == 0:
        _default(defaults)
        
    config = ConfigParser.ConfigParser()
    config.read(aliyun_ini)
    return config

def _get(item):
    c = _config()
    return c.get("ecs", item)

def _set(item, value):
    c = config()
    c.set("ecs", item, value)

def _instanceid():
    if os.path.exists(aliyun_ecs_instanceid):
    	return open(aliyun_ecs_instanceid).read()
    else:
        return False

def _metadata():
    metadata = open(aliyun_ecs_metadata).read()
    print '@TODO:'

def main(argv):
    print argv
    print '@TODO:'

if __name__ == "__main__":
    main(sys.argv)
