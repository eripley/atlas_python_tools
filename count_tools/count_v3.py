import requests
import time
from datetime import datetime, timedelta
import urllib3
import json
import string

user_list = ['Shane.thompson@victoriaplum.com', 'manager@victoriaplumtest.com', 'ozon@cargoonline.ru', 'AdminF@atlasdelivery.io', 'mvishnyakov@starbuckscoffee.ru', 'testTT@cargoonline.ru', 'vezu_ru@atlas.io', 'test@environment.com', 'transport@company.ru', 'Yuliya.Sayapina@leroymerlin.ru', 'transcopy@cargoonline.ru', 'leroymerlincopy@cargoonline.ru', 'zhurkoas@pik-industry.ru']
pwd = 'dev'
br = 'Bearer '
mu = {'uri1' : "https://www.www.ru/oms/api/odata/order?$count=true&$filter=((DeliveryTimeSlot%2FFrom+le+2019-06-21T00:00:00Z)+or+(PickupTimeSlot%2FFrom+le+2019-06-21T00:00:00Z))+and+StateInfo%2FState+eq+'Completed'&$select=Id&$skip=0",
      'uri2' : "https://www.www.ru/oms/api/odata/order?$count=true&$filter=((DeliveryTimeSlot%2FFrom+le+2019-06-21T00:00:00Z)+or+(PickupTimeSlot%2FFrom+le+2019-06-21T00:00:00Z))+and+StateInfo%2FState+eq+'Cancelled'&$select=Id&$skip=0",
      'ruri' : "https://www.www.ru/tms/api/odata/route?$select=Id&$count=true&&$filter=(StateInfo%2FState+ne+%27Finished%27)+and+(RouteInfo%2FStart+le+2019-06-21T00:00:00Z)",
      'orori' : "https://www.www.ru/oms/api/odata/order?$count=true&$filter=((DeliveryTimeSlot%2FFrom+le+2019-06-21T00:00:00Z)+or+(PickupTimeSlot%2FFrom+le+2019-06-21T00:00:00Z))+and+StateInfo%2FState+ne+'Completed'+and+StateInfo%2FState+ne+'Cancelled'&$select=Id&$skip=0"}
new_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
oms_uri = 'https://www.www.ru/oms/api/odata/order?$count=true&$select=Id&$skip=0&$top=10000'
av = list(mu.values())                          # values for dictionary mu
ak = list(mu.keys())                            # keys for dictionary mu

rb = []
b = [] # json's datas holder
OrderFound = []
routeFound = []
token_holder = []
oms_count = []
#for num in range(len(ak)):
i=0
j=0

def PrepBody(username, password):
    body = """{
  "username": "%(usn)s",
  "password": "%(psw)s" 
}"""% {"usn" : username, "psw" : password}
    return body

for num in range(len(user_list)):                            # do not forget to change num's range!!!
    usr = user_list[num]
    psw = pwd
    ar = requests.post(url="""https://www.www.ru/auth/api/v1/Login""",
                       data=PrepBody(usr, psw).encode('utf-8'), headers=new_headers)
    d = ar.json()
    sa = str(d['sessionId'])
    #print(sa)
    wr = requests.post(url="""https://www.www.ru/auth/api/v1/Token""", headers={'Cookie': 'Auth=' + sa})
    f = wr.json()
    sf = str(f['token'])
    token = br + sf
    token_holder.append(str(token))
print(token_holder)
    #print(token)

while i <len(token_holder):
    for j in av:
        if ak[av.index(j)] != 'ruri':
            r1 = requests.get(j, headers={'Authorization': token_holder[i]})
            r_dict = r1.json()
            a = int(r_dict['@odata.count'])
            b.append(a)  # json's datas holder
        else:
            r1 = requests.get(j, headers={'Authorization': token_holder[i]})
            r_dict = r1.json()
            e = int(r_dict['@odata.count'])
            rb.append(e)
            r2 = requests.get(j, headers={'Authorization': token_holder[i]})
            oms_dict = r2.json()
            o = int(oms_dict['@odata.count'])
            print(o)
    i=i+1

OrderFound.append(sum(b))
routeFound.append(sum(rb))
print("OrdersFounds")
print(OrderFound)
print("==============")
print("routesFounds")
print(routeFound)