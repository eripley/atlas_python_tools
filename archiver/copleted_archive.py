import requests
import time
token = 'Bearer 1d75bc44109b4ea5aac3a9a600dc18b1ba6272db502c45b7b9d633c24a7c9e2c2a0d33d54d7f4cdfbaee3dd3203e4268'

array = [
    {
        "Id": "00baa327-95a4-4b50-954b-4bc17d9b0921"
    },
    {
        "Id": "2c0e4e23-e6e4-4e08-8864-a4ac463f454f"
    },
    {
        "Id": "416f031b-beba-4cb4-9cb8-b4c3092b6cd6"
    },
    {
        "Id": "5f3ed325-94fb-483a-ae92-e62d440cdb09"
    },
    {
        "Id": "64f7b966-66f2-4b8e-b29e-70066a520742"
    },
    {
        "Id": "d68d3bb3-b6ad-4f6a-a5ce-79eb7a103f8d"
    },
    {
        "Id": "e5c897bd-ff43-4724-9606-62917c415ce9"
    },
    {
        "Id": "ef64141a-b3f4-4e30-ac49-85d9578e223b"
    },
    {
        "Id": "f5ef5307-3c3e-4dd8-93ff-1b1765186771"
    }
]


i=0
while i < len(array):
    #time.sleep(1)
    OrderId = array[i]["Id"]
    #OrderId = array[i]
    print(OrderId)
    body = {"State": "Cancelled"}
    r1 = requests.put("""https://www.www.ru/oms/api/Orders/%(Id)s/StateInfo""" % {"Id": OrderId},
                      headers={'Authorization': token}, json=body)
    print(r1.status_code)

    comment = {"Title": "Reason of complete",
                "CommentType": "Manager",
                "Comment": "Техническое завершение заявки"}
                #"Comment": "The Order was autocomplete"}

    r2 = requests.post("""https://www.www.ru/oms/api/Comments/%(Id)s/Comments""" % {"Id": OrderId},
                      headers={'Authorization': token}, json=comment)
    print(r2.status_code)

    r3 = requests.delete("""https://www.www.ru/oms/api/Orders/MoveToArchiveOrder/%(Id)s""" % {"Id": array[i]["Id"]},
                      headers={'Authorization': token})
    print(r3.status_code)
    print(i*100/len(array))
    i = i+1