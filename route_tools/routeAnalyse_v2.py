import requests
import time

urlR = "https://www.www.ru/tms/api/odata/route?$select=Id&$count=true&$expand=RoutePoints($expand%3DOrderTasks($select%3DOrderId))&$filter=StateInfo%2FState+ne+%27Finished%27"
# token = 'Bearer ac2e076e77e940fda7f4a8fe011efca64723a553da79409a842a73280fa7447e20bc6976b53146089bf0444d28975979'
token_M = ['Bearer ac2e076e77e940fda7f4a8fe011efca6638af66ec90541d39553e84f8a0b8419ee9366c0e93c4589bacbd78a07444a0e', 'Bearer 197bb76aeabe488688b3aa7a00d0101620a23c97e317445d9f1565ef2b66b938fb1b0971592f4a55beedb7d3c4958994', 'Bearer fd50c5a3e6154db7b0f1aa7a00d07a5d10316489750742e68c683f5036a22013a87021692c2741b698e15db87714ec1d', 'Bearer 6c846cb0ca1d464fb794aa7a00cf221a2f8a948713f74cf4838f61549f9d24d2f927a78c82c14a6d86147e4ba85b4952', 'Bearer 58e5341f5f354bde96d9aa7a00cf5b044882d20ad336497c81701c0002a451e2dd0b9c1ffc434ddba09bb53c86ce5093']
# routeMassive =list(filter((lambda x: x['Id'] != "6e94777d-5fcc-42b5-bfe5-eb1882ff5c75"), routeMassive))
# routeMassive =list(filter((lambda x: x['Id'] != "e0d06abf-0221-4ff0-8d6d-9792e23b7d17"), routeMassive))
# routeMassive =list(filter((lambda x: x['Id'] != "e007cd33-41f4-422f-9227-ed8353d19acd"), routeMassive))
badRoutes = []
RoutesToFinish = []
routeMassive = []
i = 0
l = 0

while l < len(token_M):
    r1 = requests.get(urlR, headers={'Authorization': token_M[l]})
    ut = r1.json()["value"]
    routeMassive.append(ut)
    print(routeMassive)
    l = l + 1

while i < len(routeMassive):
    k = 0
    while k < len(routeMassive[i]):
        routeId = routeMassive[i][k]["Id"]
        orderMassive = list(map(lambda x: x["OrderTasks"][0]["OrderId"], routeMassive[i][k]["RoutePoints"]))
        j = 0
        OrdersState = []
        while j < len(orderMassive):
            order = orderMassive[j]
            print(order)
            a = 0
            # iterate by token
            while a < len(token_M):
                r2 = requests.get("""https://www.www.ru/oms/api/Orders/%(Id)s/StateInfo""" % {"Id": order},
                                  headers={'Authorization': token_M[a]})
                print(r2.status_code)
                a = a + 1
                if r2.json() == {'Message': 'Order info not found'}:
                    badRoutes.append(routeId)
                    OrdersState = []
                    j = len(orderMassive)
                else:
                    OrdersState.append(r2.json()["State"])

            j = j + 1
        if len(OrdersState) > 0:
            tmpMass = list(filter(lambda x: (x == 'Completed' or x == 'Cancelled'), OrdersState))
            if len(tmpMass) == len(OrdersState):
                RoutesToFinish.append(routeId)

        k = k + 1
        print(i * 100 / len(routeMassive))

    i = i + 1
print("Routes with problem tasks:")
print(badRoutes)
print("=====================")
print("Routes To Finish:")
print(RoutesToFinish)
# print(r1)
