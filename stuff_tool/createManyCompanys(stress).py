import requests
import time
import csv
import json
import datetime

Token = 'Bearer 4c2832e6b9cd494ea465a92f010219fdc287f05ad25e45a7b54afdf10a1e8b7f53c64d10aae5404bb52f646f8650d7be'
new_headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': Token}

SysDateTime = datetime.datetime.now()
SysDateTime = SysDateTime.strftime("%Y-%m-%d")

i=0
n=200
while i < n:
#    compName = int(round(time.time() * 1000))
    body = """{
    "Name": "%(cli)s",
    "From": "%(dateFrom)s",
    "To": "%(dateTo)s"
  }""" % {'dateFrom': SysDateTime + "T05:00:00Z", 'dateTo': SysDateTime + "T20:00:00Z", 'cli': 'COMP' + str(i)}
    r1=requests.post(url="https://www.www.ru/resources/api/consignors",
                      data=body, headers=new_headers)
#    print(r1.status_code, "{'Comp N': ", compName, "}")
    print(r1.content)
#    print(i*100/len(array))
    time.sleep(1)
    i += 1
#    print(i*100/n)