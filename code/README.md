# 

## Install

Inside a virtual environment (`conda` or `virtualenv` or whatever floats your
boat ⛵)

```
virtualenv -p /usr/bin/python3.8 env
source env/bin/activate
```

This will install BEP032tools and the Neo "bleeding edge"

```
pip install -r requirements.txt
cd lib/BEP032tools
pip install .[tools]
cd ../python_neo
python setup.py install
```
