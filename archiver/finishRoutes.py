import requests

token = 'Bearer ac2e076e77e940fda7f4a8fe011efca6eaa4d59b1eb3445887a26a8666b8d57b0294e352b433420c84b342ad1509ab1f'

routesId = ['254eada8-0090-4b69-8614-c3ed7dc655c2', '4d82ae08-26e4-4b30-9ad9-19b39c0053a1', '88e1af93-14d2-4d1f-b3a5-8b83605eaee8', 'dfa4d8cd-2b3b-48db-a8d5-75941e282bec', 'e2b1396d-76d7-411d-a463-8dd286d86c7c', 'e38a340e-36a5-4bc3-93f7-16676218e03c', 'efb053db-33f2-42fa-b0b4-5677d7da7e54', 'f668d957-8330-44ce-8093-de3dd5271791', 'feb53ba2-944f-44dd-892f-78d9202112e6', '9e25c115-d100-4a92-8988-8529d385e74b', '3b94fb73-aad5-4615-a187-b7e4cd9b001f', '440c4a38-6a53-40b0-a526-3b94786d950f', '54dabc8e-b548-471a-b712-085e58f685bc', 'a4367d29-2b04-4118-ab00-770f36a102ee', 'e7bb76e9-518f-4a1d-a16c-1804db5f4542', '11354a98-2cd2-4865-b631-4bf1e7c8b9eb', '1efeafd0-87bc-40c3-843b-0cfff0491bbf', '67d024b3-ae65-4666-8574-6b2c4e863842', '69b6afbe-ac25-4e53-94cb-2d094cfa7e7a', '87b9b3f4-bd58-47c1-a074-7b0b1cb27426', '812b8b6e-fd0f-44ad-8535-3c747f1a08f1', '9458c5e2-8a13-4e5a-a4bf-8dff2f6c67f5', 'e794c87d-473e-448c-9be9-6c3d51c48b30', 'ec607c17-00cc-47d0-ade2-f67e42857248', '03d3ca62-c00d-4b73-ba07-9e978a26854f', '1f2333bb-3181-47bd-9d48-dc507a4dbda4', '4187ca36-8d68-4b8e-9d26-b0de54614d4d', '68d0c551-b71b-4828-9977-7116a1cc1581', '7be62347-787c-418b-a926-787dafe5ddef', '8a332ea1-7498-40a7-b566-b2f34badd7da', '9abd0bba-3d38-42e2-bccd-c7b287fa4f43', '9c326595-7bce-46b1-8a56-dfaa887f472a', 'c5abf44e-6eba-4239-9546-97d0346ff470', 'e95c77a8-3ea4-45d3-ab92-230e7dd7377a', 'fc85d70c-9b76-4307-9525-078a9cd4f5a8', 'b4171a4a-b9cb-4d17-b6fb-721c8c76cdce']

body = {

  "State": "Finished"
}

i=0
while i < len(routesId):
  r1=requests.put("""https://www.www.ru/tms/api/Routes/%(Id)s/StateInfo"""%{"Id": routesId[i]}, headers = {'Authorization' : token}, json  = body)
  print(r1.status_code)
  #r2 = requests.delete( """https://www.www.ru/tms/api/Routes/MoveToArchiveRoute/%(Id)s""" % {"Id": routesId[i]["Id"]},headers={'Authorization': token})
  print(routesId[i])
  #print(r2.status_code)
  #print(r2.status_code)
  i=i+1
  