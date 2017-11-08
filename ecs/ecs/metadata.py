#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Meta for aliyun ecs
"""

import os
import sys

import logging
import ConfigParser
import argparse

import json
import requests


log_format = logging.Formatter("[%(asctime)s] %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("metadata")


class Metadata(object):
    """Metadata for aliyun ecs
    """
    url4vpc = os.getenv("URL4VPC", "http://100.100.100.200/latest/meta-data")

    def __init__(self, log_level=40):
        self.set_logging(log_level)
        
        home = os.getenv("HOME", ".")
        aliyun = os.getenv("ALIYUN", os.path.join(home, ".aliyun"))

        self.ini = os.path.join(aliyun, "config.ini")
        self.ecs_dir = os.path.join(aliyun, "ecs")
        self.instanceid_file = os.path.join(aliyun, "ecs/instanceid")

        self.exists(self.ecs_dir, isdir=True)
        self.exists(self.ini)
        self.exists(self.instanceid_file)

        self.conf = ConfigParser.ConfigParser()
        self.conf.read(self.ini)

    def set_logging(self, log_level=40):
        logger.setLevel(log_level)

        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        ch.setFormatter(log_format)

        logger.addHandler(ch)


    def exists(self, path, isdir=False):
        if os.path.exists(path):
            return True
        else:
            if isdir == True:
                logger.debug("Directory %s is not exists, creating it." % path)
                os.makedirs(path)
            else:
                logger.debug("File %s is not exists, creating it." % path)
                with open(path, "wb") as fp:
                    fp.write("")


    def has_section(self, section="ecs"):
        c = self.conf
        ini = self.ini
        if c.has_section(section) == False:
            logger.debug("Section %s is not exists, adding to %s" % (section, ini))
            with open(ini, "wb") as fp:
                c.add_section(section)
                c.write(fp)


    def set(self, item, value, section="ecs"):
        c = self.conf
        ini = self.ini
        with open(ini, "wb") as fp:
            c.set(section, item, value)
            c.write(fp)


    def get(self, item, section="ecs"):
        return self.conf.get(section, item)


    def metadata4vpc(self, url="", timeout=3, item=""):
        url4vpc = Metadata.url4vpc
        if url == "":
            url = url4vpc
        if item:
            url = os.path.join(url, item)

        logger.debug("Requesting url %s." % url)
        r = requests.get(url)
        if item:
            res = r.content.split("\r\n")
            if len(res) <= 1:
                return res[0]
            return res
        else:
            metadata = {}
            metadata_items = r.content.split("\n")
            for item in metadata_items:
                item_url = os.path.join(url4vpc, item)
                res = requests.get(item_url)
                if item.endswith("/"):
                    item = item.replace("/", "")
                    sub_items = res.content.split("\n")
                    metadata[item] = {}
                    for sub_item in sub_items:
                        sub_res = self.metadata4vpc(url=item_url, item=sub_item)
                        metadata[item][sub_item] = sub_res
                else:
                    metadata[item] = res.content
            return metadata


    def instanceid(self, url="", timeout=3):
        instanceid_file = self.instanceid_file
        if os.path.getsize(instanceid_file) == 0:
            instanceid = self.metadata4vpc(item="instance-id")
            with open(instanceid_file, "wb") as fp:
                fp.write(instanceid)
        else:
            return open(instanceid_file, "r").read()


    def listall(self):
        res = self.metadata4vpc()


def main(log_level=40):
    def process_args(argv):
        parser = argparse.ArgumentParser(
                version="%(prog)s 0.0.4",
                description="Get metadata for aliyun ecs in vpc.")
        group = parser.add_mutually_exclusive_group()

        group.add_argument("-a", "--all", action="store_true", dest="all", default=False,
                help="show all metadata of current ecs")

        group.add_argument("-i", "--instanceid", action="append_const", dest="metadata_keys", const="instance-id",
                help="show instanceid of current ecs")
        group.add_argument("-n", "--network", action="append_const", dest="metadata_keys", const="network-type",
                help="show network type of current ecs")
        group.add_argument("-e", "--eip", action="append_const", dest="metadata_keys", const="eipv4",
                help="show eip binded on current ecs")
        group.add_argument("-p", "--privateip", action="append_const", dest="metadata_keys", const="private-ipv4",
                help="show privateid of current ecs")
        group.add_argument("-V", "--vpc", action="append_const", dest="metadata_keys", const="vpc-id",
                help="show vpcid of current ecs")
        group.add_argument("-s", "--vswitch", action="append_const", dest="metadata_keys", const="vswitch-id",
                help="show vswitchid of current ecs")
        group.add_argument("-S", "--vswitch-block", action="append_const", dest="metadata_keys", const="vswitch-cidr-block",
                help="show vswitch-cidr-block of current ecs")
        group.add_argument("-z", "--zoneid", action="append_const", dest="metadata_keys", const="zone-id",
                help="show zoneid of current ecs")

        parser.add_argument("-D", "--debug", action="store_const", dest="log_level", const=logging.DEBUG,
                help="show debug information (set logging as logging.DEBUG)")

        return parser.parse_args(argv)

    results = process_args(sys.argv[1:])
    if results.all == False and results.metadata_keys == None:
        process_args(["-h"])
        sys.exit(1)
    
    if results.log_level:
        log_level = results.log_level

    e = Metadata(log_level)

    if results.all == True:
        res = e.metadata4vpc()
        item_len = len(max(res.keys(), key=len)) + 2
        value_len = len(max(res.values(), key=len)) + 2
        print 'Name'.center(item_len, '-'), 'Metadata'.center(value_len, '-')
        for item in res:
            if isinstance(res[item], str):
                key = ''.join([item, ':'])
                print key.rjust(item_len, ' '), res[item].ljust(value_len, ' ')
        print "-" * (item_len + value_len + 1)
    else:
        for item in results.metadata_keys:
            print e.metadata4vpc(item=item)



if __name__ == "__main__":
    main()
