from urllib import parse

import requests

# url = 'http://httpbin.org/post'
# headers={'content-type': 'application/json'}
# r = requests.post(url)
# print(r.text)

import csv
import os

import requests

session = requests.Session()

filePath = '/home/xjye/PycharmProjects/downsheet/1.2.276.0.7230010.3.2.1868790/1.2.156.112605.14038004227650.20160531220346.3.8820.5/1.2.156.112605.14038004227650.20160531220510.4.7820.1.dcm'
instanceUploadUrl ="http://localhost:8091/api/v1.0.3/batch/{}/instance"

res = session.post(
    instanceUploadUrl.format("testxin002"),
    data=open(filePath,
              'rb')).json()
print(res)