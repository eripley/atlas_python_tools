import time
import requests
import uuid
import datetime
import _json
import psycopg2
from psycopg2 import sql

array = [
{"Id":"9fd8c56e-2558-4d83-b1f6-1f6dfb9c86de","ParentCompanyId":"d7be785e-c270-4273-871a-a92f010219fd","Name":"COMP40","From":"2019-03-20T05:00:00Z","To":"2019-03-20T20:00:00Z"}
]
table = 'Presets'
lolly = 'chain'

i=0
#while i < len(array):
conn = psycopg2.connect(dbname='moloch-dev', user='postgres', password='PriemPgsql!', host='10.10.122.103')
cursor = conn.cursor()
cursor.execute("set search_path = 'dbo'")
cursor.execute("""UPDATE "Companies"
                set "Settings" = "Settings" ::jsonb - 'SendSms' || '{"SendSms" : false}' ::jsonb
                where "Id" = %(Id)s;""", {'Id': array[i]["Id"]})
#cursor.execute('SELECT * FROM "Presets" WHERE "Id" = company ;')
records = cursor.fetchall()
cursor.close()
conn.close()
print(records)
