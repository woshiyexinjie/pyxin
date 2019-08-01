import urllib.request
import tarfile
import os
import json
from urllib import request


url_series = ""
r = urllib.request.urlopen(url_series)
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
result = data['result']
print(result)