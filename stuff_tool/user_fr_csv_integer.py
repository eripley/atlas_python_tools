import psycopg2

company = 'd7be785e-c270-4273-871a-a92f010219fd'
conn = psycopg2.connect(dbname='moloch-dev', user='postgres',
                        password='PriemPgsql!', host='10.10.122.103')
cursor = conn.cursor()
cursor.execute("set search_path = 'dbo'")
cursor.execute("""SELECT * FROM "Companies" WHERE "Id" = 'd7be785e-c270-4273-871a-a92f010219fd';""")
records = cursor.fetchall()
print(records)

-----------

# coding: utf-8
import psycopg2
import uuid
import requests
import json
import random
import sys
import time
import csv

m_urls ={"login": "https://www.www.ru/api/Account/Login",
         "postUser": "https://www.www.ru/api/users/post"}
loginData = "{'Email': 'test@environment.com', 'Password': 'qa_test'}"
headers = {"Content-Type" : "application/json; charset=UTF-8",
           "accept-language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
           "accept-encoding":"gzip, deflate, br"}
r = requests.post(url=m_urls["login"], data=loginData, headers=headers)
print(r.status_code)
cookie = {'.DELIVERATOR_AUTH': r.cookies[".DELIVERATOR_AUTH"]}

ConnString = {'qa' : "host='10.10.122.103' dbname='priem-transvalair-qa' user='postgres' password='PriemPgsql!'",
				'dev' : "host='10.10.122.103' dbname='priem-transvalair-dev' user='postgres' password='PriemPgsql!'",
                'demo' : "host='10.10.122.103' dbname='priem-transvalair-demo' user='postgres' password='PriemPgsql!'",
                'prod_lm' : "host='10.10.121.103' dbname='platform-master' user='postgres' password='Lkz5343ghjlf$1'"}

HubId ='03056324-fd17-4be1-84f7-24e028302bcd'
PlatfName = 'prod_lm'

def conncentToDB(self):
	conn = psycopg2.connect(ConnString[self])
	return conn

def getUsernamePassword(PlatfName, HubId):
    openDB = conncentToDB(PlatfName)
    cursor = openDB.cursor()
    cursor.execute("set search_path = 'dbo'")
    cursor.execute("""DELETE from "Users"\
                        where "DeletedBy" is null\
                        and "CompanyId" ='%(HubId)s'\
                        and "Settings"::json#>> '{Roles, 0}' = 'GlobalObserver';"""% {'HubId': HubId})
    cursor.execute("commit")
    return "Ok"


print(getUsernamePassword(PlatfName, HubId))

fieldnames = ['Surname','Name','Username','Pass']
with open('newUsers.csv', encoding='windows-1251') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        newUserData = """{
          "CompanyId": "%(HubId)s",
          "Email": "%(email)s",
          "Id": null,
          "Password": "%(pass)s",
          "Roles": [
            "GlobalObserver"
          ],
          "Username": "%(email)s",
          "FirstName": "%(name)s",
          "LastName": "%(surname)s"
        }""" % {'email': row['Username'], 'pass':row['Pass'], 'name':row['Name'], 'surname':row['Surname'], "HubId": HubId}

        r1 = requests.post(url=m_urls['postUser'], cookies=cookie, headers=headers,
                           data=newUserData.encode('utf-8'))
        print(r1.text)
        print(r1.status_code)

