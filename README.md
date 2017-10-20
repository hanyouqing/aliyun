# aliyun

A set of tools for aliyun.

## Installing

### Install Virtualenv (recommend)

```bash
pip install virtualenv

pip install virtuanenvwrapper

touch ~/.bashrc
grep virtualenvwrapper.sh ~/.bashrc || echo 'source $(which virtualenvwrapper.sh)' >> ~/.bashrc
source ~/.bashrc

mkvirtualenv aliyun
```


### Aliyun Ecs Tools

Some of the need to set config(see [Config](cofnig/README.md)).

**Building**

```bash
git clone https://github.com/teachmyself/aliyun.git
cd aliyun/ecs 
./package.sh pack
pip install dist/aliyun_ecs-0.0.1.tar.gz
```

**Installing by pip**

```bash
pip install aliyun-ecs
```

**Usage**

```bash
ecs-metadata4vpc
```


## Reference

### Package

This is a simple demo.

**Directory Tree of aliyun-ecs**

```bash
├── LICENSE                  # License file
├── MANIFEST.in              # 
├── Makefile
├── README.txt
├── metadata
│   ├── __init__.py
│   └── vpc.py
├── package.sh
├── requirements.txt
├── setup.cfg
└── setup.py
```

* [LICENSE]()
* [MANIFIFEST.in]()
* [Makefile]()
* [README.txt]()
* [requirements.txt]()
* [setup.cfg]()
* [setup.py]()


* [](https://wiki.python.org/moin/CheeseShopTutorial#Package_Meta-Data)
