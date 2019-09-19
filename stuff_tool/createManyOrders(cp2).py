import requests
import time
import datetime
import random

SysDateTime = datetime.datetime.now()
SysDateTime = SysDateTime.strftime("%Y-%m-%d")


def PrepairBody(number): #боди заявки
    body ="""{
    "OrderInfo": {
        "ExternalId": "%(number)s",
        "Number": "%(number)s",
        "OriginalAddress": "%(addres)s",
        "OperationType": "Delivery"},
    "AllocationInfo": {
        "HubCode": "%(postcode)s",
        "CarrierCode": "%(postcode)s"
        },
    "AddressInfo": {
            "FullAddress": "%(addres)s",
            "Country": "",
            "PostalCode": "%(postcode)s",
            "Region": "",
            "District": "",
            "Town": "",
            "TownRegion": "",
            "Street": "",
            "Station": "",
            "Building": "",
            "Housing": "",
            "Porch": "",
            "Floor": "",
            "Room": ""
        },
    "DeliveryTimeSlot": {
        "From": "%(dateStart)s",
        "To": "%(dateEnd)s"
    },
    "ContactInfo": {
        "Name": "%(name)s",
        "Phones": [
            "+7 926 219-07-23"
        ],
        "Emails": [
            "ml@uniteller.ru"
        ]
    },
    "Products": [
        {
            "ExternalId": "PRDT00",
            "Name": "%(product)s",
            "Article": "PRDT00",
            "Note": null,
            "PhotoUrl": null,
            "Unit": null,
            "Quantity": 3,
            "Volume": 0,
            "Weight": 33,
            "Tax": 0,
            "TaxRate": 20,
            "Price": 0.3,
            "PriceWithoutTax": 0.3,
        },
        {
            "ExternalId": "PRDT00",
            "Name": "%(product)s",
            "Article": "PRDT00",
            "Note": null,
            "PhotoUrl": null,
            "Unit": null,
            "Quantity": 11,
            "Volume": 0,
            "Weight": 33,
            "Tax": 0,
            "TaxRate": 20,
            "Price": 0.9,
            "PriceWithoutTax": 0.9,
        }   
      ],
    "Payment": {
            "PaymentStateInfo": {
                "PaymentState": "NotPayed"	
            },
            "Payments": []
        },
    "Services": [
        {
            "Name": "Delivery",
            "Article": "SRVC01",
            "Note": null,
            "Unit": null,
            "Quantity": 1,
            "Price": 0.25,
            "PriceWithoutTax": 0.25,
            "Tax": 13,
            "TaxRate": 20
        },
        {
            "Name": "Liftup",
            "Article": "SRVC01",
            "Note": null,
            "Unit": null,
            "Quantity": 1,
            "Price": 0.25,
            "PriceWithoutTax": 0.25,
            "Tax": 13,
            "TaxRate": 20
        }
  ],

    "ServiceInfo": {
        "DeliveryPrice": "0.15",
        "LiftupPrice": "0.10"
    }
}"""%{"number": number,
      "addres": random.choice (["переулок Ангелов переулок д. 8", "Самотёчная улица, 15, Москва, Россия. 127473", "Кутузовский проспект д. 26к1", "1-й Самотечный переулок, 15, Москва, Россия. 127473"]),
      "name": "Иван Иванов",
      "product": random.choice (["Гипсокартон влагостойкий Knauf ГСП-Н2 2500x1200х9.5 мм", "Гуталин промышленный", "Гель для отверстий 1л", "Перчатки резиновые", "Затирка для трещин"]),
      "postcode" : random.choice (["6101"]),
      "carrier" : "38030",
      "dateStart": SysDateTime + "T05:00:00Z",
      "dateEnd": SysDateTime + "T23:00:00Z"}
    return body
Token = 'Bearer 01745547a4fd4b19919caa8700685b115253095029d14dd1af6a3b74c4664ebb944e88eb9d184581a4543a1654753d0d' #берем токен с фронта
i = 0
n = 10
while i < n:
    OrderNumber = int(round(time.time() * 1000))
    new_headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': Token}
    r3 = requests.post(url="https://www.www.ru/oms/api/Orders",
                       data=PrepairBody(OrderNumber).encode('utf-8'), headers=new_headers)
    print(r3.status_code, "{'Order N': ",OrderNumber, "}")
    time.sleep(1)
    i +=1
    print(i*100/n)