#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


NAME             = "aliyun_ecs"
VERSION          = open("VERSION").read().replace("\n", "")
KEYWORDS         = ("aliyun", "ecs", "metadata", "vpc", "teachmyself")
DESCRIPTION      = "A set of simple tools for aliyun ecs."
LONG_DRSCRIPTION = open("README.rst").read()
LICENSE          = "MIT LICENSE"
URL              = "https://github.com/teachmyself/aliyun/ecs"
AUTHOR           = "teachmyself"
AUTHOR_EMAIL     = "teachmyself@126.com"
PACKAGES         = find_packages()
INSTALL_REQUIRES = ["requests"]
TEST_SUITE       = ""
SCRIPTS          = []
CONSOLE_SCRIPTS  = [
    "ecs-metadata4vpc = ecs.metadata:main",
]

setup(
    name = NAME,
    version = VERSION,
    keywords = KEYWORDS,
    description = DESCRIPTION,
    long_description = LONG_DRSCRIPTION,
    license = LICENSE,

    url = URL,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,

    packages = PACKAGES,
    install_requires = INSTALL_REQUIRES,
    test_suite = TEST_SUITE,

    scripts = SCRIPTS,
    entry_points = {
        "console_scripts": CONSOLE_SCRIPTS
    }
)
