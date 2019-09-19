import requests
import time


Token = 'Bearer 4c2832e6b9cd494ea465a92f010219fdb632ff25e7364c1c925a71503e89c387fcbadb2c120e4c2cafeacd0a93c2dc7e'
new_headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': Token}

array = [
]


i=0
while i < len(array):
    body = """{"Id": "%(Id)s",
            "Comment": "qa"}""" % {"Id": array[i]["Id"]}
    r1=requests.delete(url="https://www.www.ru/api/companies/delete",
                      data=body, headers=new_headers)
    print(r1.status_code)
    print(i*100/len(array))
    time.sleep(0.5)
    i=i+1