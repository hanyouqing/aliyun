# aliyun

A set of tools for aliyun.

## Installing

### Install Virtualenv (recommend)

```bash
pip install virtualenv

pip install virtuanenvwrapper

source $(which virtualenvwrapper.sh)
grep virtualenvwrapper.sh ~/.bashrc || echo 'source $(which virtualenvwrapper.sh)' >> ~/.bashrc

mkvirtualenv aliyun
```

### Installing tools

```bash
pip install ecs-metadata4vpc
```

## Usage

```bash
ecs-metadata4vpc
```
