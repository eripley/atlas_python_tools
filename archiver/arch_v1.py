import requests
import time
token = 'Bearer 142318e547df4f3c8cf5a97c00dd1ea07a61bcb5ebda44d4a8c0a1d034c05ffc0f165cd7f6154a22a0018f90feab9848'

array = [
  ]

i=0
while i < len(array):
   #time.sleep(0.5)
   #OrderId = array[i]["Id"]
   #print(OrderId)
   # body = {"State": "NotGeocoded"}
   # r12 = requests.put("""https://www.www.ru/oms/api/Orders/%(Id)s/StateInfo""" % {"Id": array[i]["Id"]},
   #                   headers={'Authorization': token}, json=body)
   # print(r12.status_code)
   r1 = requests.delete("""https://www.www.ru/oms/api/Orders/MoveToArchiveOrder/%(Id)s""" % {"Id": array[i]["Id"]},
                     headers={'Authorization': token})
   print(r1.status_code)
   print(i*100/len(array))
   i = i+1