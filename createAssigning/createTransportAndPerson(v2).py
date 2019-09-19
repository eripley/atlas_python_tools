import time
import csv
import json
import datetime
import requests

SysDateTime = datetime.datetime.now()
SysDateTime = SysDateTime.strftime("%Y-%m-%d")

token = 'Bearer d747dcbd13154f7d91fbaa6200e98be1bdb4ead91a8b466098f02489c48c4f09b3e24a8978ea459d839e28d2e335b77a'
new_headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization' : token}
i=0

getComp = requests.get(url="""https://www.www.ru/resources/api/companies/All""", headers={'Authorization' : token})
compMass = getComp.json()
compTmp = []
#print(m)
fieldnames = ['Company', 'Type', 'Trademark', 'Number', 'Color', 'Volume',
              'Cost', 'TakesTime', 'Weight', 'Username']
with open('azb.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for json in compMass:
            n = str(json['Id'])
            m = str(json['Name'])
            if row["Company"] == m:
                print(row["Company"])
                transType = row["Type"]
                transMark = row["Trademark"]
                transNumber = row["Number"]
                transColor = row["Color"]
                transVolume = row["Volume"]
                transCost = row["Cost"]
                transTime = row["TakesTime"]
                transWeight = row["Weight"]
                personName = row["Username"]
                bodyPerson = """{
                  "CompanyId": "%(Id)s",
                  "CreatedOn": null,
                  "EndDelivery": "%(endDeliv)s",
                  "EndLunch": "%(endLunch)s",
                  "FirstName": "%(pname)s",
                  "LastName": "%(pname)s",
                  "NicName": "%(pname)s",
                  "Password": "%(pname)s",
                  "Patronymic": null,
                  "StartDelivery": "%(startDeliv)s",
                  "StartLunch": "%(startLunch)s",
                  "Username": "%(pname)s",
                  "Rating": null,
                  "Roles": [
                    "Courier"
                  ],
                  "Tags": []
                }""" % {'Id': n, 'pname': personName, 'endDeliv': SysDateTime + "T20:00:00Z",
                        'endLunch': SysDateTime + "T12:00:00Z", 'startDeliv': SysDateTime + "T07:00:00Z",
                        'startLunch': SysDateTime + "T11:00:00Z"}
                r2 = requests.post(url="""https://www.www.ru/api/persons/post""", data=bodyPerson.encode('utf-8'), headers=new_headers)
                personId = r2.json()
                print(r2.status_code)
                print(r2.content)
                bodyTransport = """{
                    "AvailableLoadUnloadTypes": [],
                    "Color": "%(col)s",
                    "CompanyId": "%(Id)s",
                    "Cost": %(cost)s,
                    "Id": null,
                    "Number": "%(num)s",
                    "TakesTime": %(take)s,
                    "Trademark": "%(mark)s",
                    "TransportRestrictions": [
                        "СК",
                        "ТТК",
                        "МКАД"
                    ],
                    "Type": "%(tp)s",
                    "Volume": %(vl)s,
                    "Weight": %(wg)s,
                    "PreferredPersonIds": [
                        "%(prf)s"
                    ],
                    "Tags": [
                        {
                            "Name": "7tonns",
                            "Type": "CarRequiredPersonLicence"
                        },
                        {
                            "Name": "3tonns",
                            "Type": "CarRequiredPersonLicence"
                        }
                    ]
                }""" % {'Id': n, 'prf': personId, 'col': transColor, 'cost': transCost, 'num': transNumber,
                        'take': transTime, 'mark': transMark,
                        'tp': transType, 'vl': transVolume, 'wg': transWeight}
                r3 = requests.post(url="""https://www.www.ru/api/transport/post""", data=bodyTransport.encode('utf-8'), headers=new_headers)
                print(r3)
                print(r3.status_code)
                print(r3.content)