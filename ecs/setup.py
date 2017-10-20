#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "aliyun_ecs",
    version = "0.0.2",
    keywords = ("aliyun", "ecs", "metadata", "vpc", "teachmyself"),
    description = "A set of simple tools for aliyun ecs.",
    long_description = open("README.txt").read(),
    license = "MIT LICENSE",

    url = "https://github.com/teachmyself/aliyun/ecs",
    author = "teachmyself",
    author_email = "teachmyself@126.com",

    packages = find_packages(),
    install_requires = ["requests"],
    test_suite = "",

    scripts = [],
    entry_points = {
        "console_scripts": [
            "ecs-metadata4vpc = metadata.vpc:main",
        ],
    }
)
