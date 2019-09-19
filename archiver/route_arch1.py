import requests


token = 'Bearer 5ea3d44d6b2d4452a94ba9dd00f3c8755834bcba23f84baa9b0030c0e98503fc951677cd436c4f299afc08d1a636c512'

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
   r1 = requests.delete("""https://www.www.ru/tms/api/Routes/MoveToArchiveRoute/%(Id)s""" % {"Id": array[i]["Id"]},
                     headers={'Authorization': token})
   print(r1.status_code)
   print(i*100/len(array))
   i = i+1
#   r2=requests.delete("""https://www.www.ru/tms/api/Routes/MoveToArchiveRoute/%(Id)s""", headers = {'Authorization' : token})
 #  print(r2.status_code)
