import requests
import time
import csv
import json
import datetime

Token = 'Bearer 4c2832e6b9cd494ea465a92f010219fdfa5a8440160545d8a2786990223710db103f98325ded41efacc56d5f0dfcde3c'
new_headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': Token}

SysDateTime = datetime.datetime.now()
SysDateTime = SysDateTime.strftime("%Y-%m-%d")
fieldnames = ['Clients', 'Code', 'Addr', 'Lt', 'Lng']
with open('cong.csv', encoding='utf-8') as csv1:
    reader = csv.DictReader(csv1)
    #        reader = csv.reader(csv1)
    #        line_count = 0
    for row in reader:
        body = """{
    "TownCode": "%(code)s",
    "Name": "%(cli)s",
    "From": "%(dateFrom)s",
    "To": "%(dateTo)s",
    "StorageLatitude": "%(lt)s",
    "StorageLongitude": "%(lng)s",
    "Address": "%(addr)s",
        }""" % {'dateFrom': SysDateTime + "T00:00:00Z", 'dateTo': SysDateTime + "T20:59:00Z",
          'code': row['Code'], 'cli': row['Client'] + " ГО", 'lt': row['Lt'], 'lng': row['Lng'], 'addr': row['Addr']}
        r3 = requests.post(url="https://www.www.ru/resources/api/consignors",
                      data=body.encode('utf-8'), headers=new_headers)
#CurrentMethod = CreateCarrier('dsn.csv')
#print(CurrentMethod)

        print(r3.status_code)
        print(r3.content)
        time.sleep(1)
