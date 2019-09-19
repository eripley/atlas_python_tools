import time
import csv
import json
import datetime
import requests

SysDateTime = datetime.datetime.now()
SysDateTime = SysDateTime.strftime("%Y-%m-%d")

token = 'Bearer 55c116ff3cb74285a936a45600f33c50acd649d56e8740a5a4177160af2a544260d4b7d72f96492d85c2df894f2f1883'
new_headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization' : token}
i=0
getRoutes = requests.get(url="""https://www.www.ru/tms/api/odata/route?$select=Id&$count=true&&$filter=(StateInfo%2FState+eq+%27Finished%27)+and+(RouteInfo%2FEnd+le+2019-07-23T00:00:00.000Z)""",
                       headers={'Authorization' : token})
routeMass = getRoutes.json()["value"]

while i < len(routeMass):
        routeid = routeMass[i]["Id"]
        body = {

            "State": "Finished"
        }
        #r1=requests.put("""https://www.www.ru/tms/api/Routes/%(Id)s/StateInfo"""%{"Id": routeid}, headers = {'Authorization' : token}, json  = body)
        #print(r1.status_code)
        r2 = requests.delete(
            """https://www.www.ru/tms/api/Routes/MoveToArchiveRoute/%(Id)s""" % {"Id": routeid},
            headers={'Authorization': token})
        print(routeid)
        print(r2.status_code)
        # print(r2.status_code)
        i = i + 1