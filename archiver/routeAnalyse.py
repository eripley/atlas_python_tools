import requests
import time

urlR = "https://www.www.ru/tms/api/odata/route?$select=Id&$count=true&$expand=RoutePoints($expand%3DOrderTasks($select%3DOrderId))&$filter=StateInfo%2FState+ne+%27Finished%27"
token = 'Bearer ac2e076e77e940fda7f4a8fe011efca6eaa4d59b1eb3445887a26a8666b8d57b0294e352b433420c84b342ad1509ab1f'
r1 = requests.get(urlR, headers = {'Authorization' : token})
routeMassive = r1.json()["value"]
# routeMassive =list(filter((lambda x: x['Id'] != "6e94777d-5fcc-42b5-bfe5-eb1882ff5c75"), routeMassive))
# routeMassive =list(filter((lambda x: x['Id'] != "e0d06abf-0221-4ff0-8d6d-9792e23b7d17"), routeMassive))
# routeMassive =list(filter((lambda x: x['Id'] != "e007cd33-41f4-422f-9227-ed8353d19acd"), routeMassive))
i = 0
badRoutes = []
RoutesToFinish = []
while i < len(routeMassive):
    routeId= routeMassive[i]["Id"]
    # print(list(map(lambda x: x["OrderTasks"][0]["OrderId"], routeMassive[i]["RoutePoints"])))
    # print("===================")
    orderMassive= list(map(lambda x: x["OrderTasks"][0]["OrderId"], routeMassive[i]["RoutePoints"]))
    j= 0
    print(orderMassive)
    OrdersState = []
    while j< len(orderMassive):
        order=orderMassive[j]
        print(order)
        r2=requests.get("""https://www.www.ru/oms/api/Orders/%(Id)s/StateInfo"""%{"Id": order}, headers = {'Authorization' : token})
        print(r2.status_code)
        if r2.json() == {'Message': 'Order info not found'}:
            badRoutes.append(routeId)
            OrdersState = []
            j= len(orderMassive)
        else:
            OrdersState.append(r2.json()["State"])
        j= j+1
    if len(OrdersState)> 0:
        tmpMass = list(filter(lambda x : (x == 'Completed' or x=='Cancelled'), OrdersState))
        if len(tmpMass) == len(OrdersState):
            RoutesToFinish.append(routeId)
    i = i +1
    print(i*100/len(routeMassive))
print("Routes with problem tasks:")
print(badRoutes)
print("=====================")
print("Routes To Finish:")
print(RoutesToFinish)
#print(r1)