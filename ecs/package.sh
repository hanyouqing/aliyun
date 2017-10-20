#!/bin/bash
#
###################################################################
# @filename:    package.sh
# @usage:       Used to package and upload a python project.
# @depedence:
# @reference:
#     python setup.py --help-commands
#     python setup.py test
#     python setup.py bdist_egg    # take .egg package, support easy_install
#     python setup.py sdist        # take .tar.gz package, support pip
#     python setup.py sdist upload
#
#  Check:
#     https://github.com/pypa/readme_renderer
# Uploading:
#     https://packaging.python.org/guides/migrating-to-pypi-org/#uploading
###################################################################
#
export PATH=.:$PATH

set -xue


package_log="package.log"


_msg() {
    echo "[$(date '+%F %T%z')] ${@}" | tee -a ${package_log}
}

_check() {
    _msg "Checking by 'https://github.com/pypa/readme_renderer'"
    python setup.py check -r -s | tee -a ${package_log}
}

_build() {
    _msg "Packging by 'python setup.py sdist'"
    python setup.py sdist | tee -a ${package_log}
}

_test() {
    _msg "Testing by 'python setup.py test'"
    python setup.py test | tee -a ${package_log}
}

_upload() {
    _msg "Uploading by 'twine upload dist/*'"
    #python setup.py sdist upload | tee -a ${package_log}
    twine upload dist/*
}

_clean() {
    _msg "Cleanling"
    rm -rf aliyun_ecs.egg-info
    rm -rf dist
    rm -rf .egg
    rm -rf package.log
}

_auto() {
    set +x
    _clean
    _check
    _test
    _build
    echo ""
    echo "You can upload by: $0 upload"
    echo ""
}

_help() {
    set +x
    echo ""
    echo "Usage: $0 [help|check|test|build|upload|clean|auto]"
    echo "	$0 help"
    echo "	$0 check"
    echo "	$0 test"
    echo "	$0 build"
    echo "	$0 upload"
    echo "	$0 clean"
    echo "	$0 auto"
    echo ""
}

if [[ ${#} -ne 1 ]]; then
    _help
else
    _$1
fi

