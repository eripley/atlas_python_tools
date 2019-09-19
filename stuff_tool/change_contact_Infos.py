import time
import csv
import json
import datetime
import requests

SysDateTime = datetime.datetime.now()
SysDateTime = SysDateTime.strftime("%Y-%m-%d")

token = 'Bearer 1c75bc44109b4ea5aac3a9a600dc18b10c1d79c4a09245b8adf1f4dcc005960007fe89a8c3c54ce0ba32d998ec22116e'
new_headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization' : token}
i=0
getRoutes = requests.get(url="""https://www.www.ru/oms/api/odata/order?$count=true&$select=Id&$skip=0""",
                       headers={'Authorization' : token})
taskMass = getRoutes.json()["value"]

while i < len(taskMass):
        taskid = taskMass[i]["Id"]
        body = {
          "Phones": [
            "74329995799",
            "74329995799"
          ]
        }
        #r1=requests.put("""https://www.www.ru/tms/api/Routes/%(Id)s/StateInfo"""%{"Id": routeid}, headers = {'Authorization' : token}, json  = body)
        #print(r1.status_code)
        r2 = requests.put(
            """https://www.www.ru/oms/api/Orders/%(Id)s/ContactInfo""" % {"Id": taskid},
            headers={'Authorization': token}, json = body)
        print(taskid)
        print(r2.status_code)
        # print(r2.status_code)
        i = i + 1