# DjangoTutorial

This repository corresponds to the Django tutorial series on my blog: https://davidfozo.com/blog/

## Overview

On my blog there is a tutorial series for beginners, where you can learn Django with current best practices like TDD. I try to be concise and practical yet, points out the bigger picture when needed. Every lesson has their own branch, so you can start at any exercise.

## Installation

Follow these steps to clone my repository from github and make the tutorial setup on your computer. Replace branch “exerciseX” with your current exercise branch. Type in these commands into your terminal:
``` 
mkdir -p DjangoTutorial/{static,virtualenv,source,database,media}
virtualenv --python=python3 DjangoTutorial/virtualenv/
git clone https://github.com/fozodavid/DjangoTutorial.git --branch exerciseX --single-branch DjangoTutorial/source
cd DjangoTutorial/source
touch MyTutorial/local_settings.py
```
 
***MyTutorial/local_settings.py***
```python
import os

from MyTutorial.settings import BASE_DIR

SECRET_KEY = 'rf@7y-$2a41o+4&z$ki0&=z)(ao=@+$fseu1f3*f=25b6xtnx$'

DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'..','database','db.sqlite3'),
    }
}
```

Finish installation with the following shell commands:
```
git branch -m exerciseX master
source ../virtualenv/bin/activate
pip install django==1.10
deactivate
```
