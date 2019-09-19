import requests
import time
from datetime import datetime, timedelta
import urllib3
import json
import string

br = 'Bearer '
print('Hello.Show me your hands:')
username = str(input())
print('login OK')
password = str(input())
print('password OK')

def PrepBody(username, password):
    body = """{
  "username": "%(usn)s",
  "password": "%(psw)s" 
}"""% {"usn" : username, "psw" : password}
    return body


new_headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
ar = requests.post(url="""https://www.www.ru/auth/api/v1/Login""",data=PrepBody(username,password).encode('utf-8'), headers=new_headers)
d = ar.json()
sa = str(d['sessionId'])
#print(sa)
wr = requests.post(url="""https://www.www.ru/auth/api/v1/Token""", headers={'Cookie' : 'Auth='+sa})
f = wr.json()
sf = str(f['token'])
token = br+sf
#print(token)

uri1 = "https://www.www.ru/oms/api/odata/order?$count=true&$filter=((DeliveryTimeSlot%2FFrom+le+2019-06-19T00:00:00Z)+or+(PickupTimeSlot%2FFrom+le+2019-06-19T00:00:00Z))+and+StateInfo%2FState+eq+'Completed'&$select=Id&$skip=0"
uri2 = "https://www.www.ru/oms/api/odata/order?$count=true&$filter=((DeliveryTimeSlot%2FFrom+le+2019-06-19T00:00:00Z)+or+(PickupTimeSlot%2FFrom+le+2019-06-19T00:00:00Z))+and+StateInfo%2FState+eq+'Cancelled'&$select=Id&$skip=0"
ruri = "https://www.www.ru/tms/api/odata/route?$select=Id&$count=true&&$filter=(StateInfo%2FState+ne+%27Finished%27)+and+(RouteInfo%2FStart+le+2019-06-19T00:00:00Z)"
orori = "https://www.www.ru/oms/api/odata/order?$count=true&$filter=((DeliveryTimeSlot%2FFrom+le+2019-06-19T00:00:00Z)+or+(PickupTimeSlot%2FFrom+le+2019-06-19T00:00:00Z))+and+StateInfo%2FState+ne+'Completed'+and+StateInfo%2FState+ne+'Cancelled'&$select=Id&$skip=0"

r1 = requests.get(uri1, headers = {'Authorization' : token})
r2 = requests.get(uri2, headers = {'Authorization' : token})
r3 = requests.get(ruri, headers = {'Authorization' : token})
r4 = requests.get(orori, headers = {'Authorization' : token})
i=0
OrderFound = []
routeFound =[]

r_dict = r1.json()
r_dict2 = r2.json()
o_dict = r3.json()
ro_dict = r4.json()
a = int(o_dict['@odata.count'])
c = int(r_dict2['@odata.count'])
m = int(o_dict['@odata.count'])
e = int(ro_dict['@odata.count'])
OrderFound.append(a+c+m)
routeFound.append(e)
print("OrdersFounds")
print(OrderFound)
print("==============")
print("routesFounds")
print(routeFound)