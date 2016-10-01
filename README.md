# django-zip-stream
[![Build Status](https://travis-ci.org/travcunn/django-zip-stream.svg?branch=master)](https://travis-ci.org/travcunn/django-zip-stream) [![codecov](https://codecov.io/gh/travcunn/django-zip-stream/branch/master/graph/badge.svg)](https://codecov.io/gh/travcunn/django-zip-stream) [![Code Health](https://landscape.io/github/travcunn/django-zip-stream/master/landscape.svg?style=flat)](https://landscape.io/github/travcunn/django-zip-stream/master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/be7b93a01ebb4fb39aa3cbdfdabfccd9)](https://www.codacy.com/app/tcunningham/django-zip-stream?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=travcunn/django-zip-stream&amp;utm_campaign=Badge_Grade)

Django extension to assemble ZIP archives dynamically using Nginx with [mod_zip](https://github.com/evanmiller/mod_zip).

## Examples
##### Django view that streams a zip with 2 files
```python
from django_zip_stream import TransferZipResponse

def download_zip(request):
    files = [
       ("/chicago.jpg", "/home/travis/chicago.jpg", 4096),
       ("/portland.jpg", "/home/travis/portland.jpg", 4096),
    ]
    return TransferZipResponse(filename='download.zip', files=files)
```
