# OreoPy

Simple and fast ORM for python.

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/maclinchy/oreopy/blob/master/LICENSE)

## Installation

There are two ways to install:

- **Install OreoPy from PyPI (recommended):**
```sh
pip install oreopy
```

- **Install OreoPy from GitHub source:**
```sh
git clone https://github.com/maclinchy/oreopy.git
cd oreopy
sudo python3 setup.py install
```

------------------
## Getting started

Let's create a file called `models.py`
```python3
from oreopy.models import base
from oreopy.fields import IntegerField, TextField

class Album(base.Model):
    title = TextField()
    artist = TextField()
    year = IntegerField()
    
album = Album()
album.create_table()
```

New record in database:
```python3
from models import Album


new_album = Album(title="Hits", artist="deadmau5", year=2018)
new_album.save()
```

Update record in database:
```python3
upd_album = Album(title="Greatest Hits")
upd_album.update(pk=1)
```

Delete record from database:
```python3
del_album = Album()
del_album.delete(pk=1)
```
