import requests
import time
import csv
import json

Token = 'Bearer 4c2832e6b9cd494ea465a92f010219fdfa5a8440160545d8a2786990223710db103f98325ded41efacc56d5f0dfcde3c'
new_headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': Token}

with open('dsn.csv', encoding='utf-8') as csv1:
#        reader = csv.reader(csv1)
#        line_count = 0
    for line in csv1:
        N = str(line)
        L = N.find('\n')
        N1 = N[:L]
        N2 = N1 + " ГП"
        body = """{"Name": "%s"}""" %N2
        print(body)
        r3 = requests.post(url="https://www.www.ru/resources/api/carriers",
                       data=body.encode('utf-8'), headers=new_headers)
#CurrentMethod = CreateCarrier('dsn.csv')
#print(CurrentMethod)

        print(r3.status_code)
        print(r3.content)
        time.sleep(1)
