from urllib import parse

import requests

url = 'http://httpbin.org/post'
headers={'content-type': 'application/json'}
r = requests.post(url)
print(r.text)