roads = [
    {'From':'A','To':'B','Distance':7},
    {'From':'A','To':'C','Distance':12},
    {'From':'B','To':'C','Distance':10},
    {'From':'B','To':'D','Distance':15}
]

#1
def cityLists(roads) :
    data_road = set()
    for row in roads :
        data_road.update(row['From'],row['To'])
    
    return data_road

result = cityLists(roads)
# print(result)

print("--------------------------")

#2
def road_from(roads,city) :
    data_road = list()
    for road in roads :
        if road['From'] == city :
            data_road.append(road)
    return data_road

result_2 = road_from(roads,'B')
# print(result_2)

print("--------------------------")

#3

import random

num_city = int(input("Enter num of cities : "))
num_road = int(input("Enter num of road : "))
first_city = 'A'
cities = set()
for nc in range(0,num_city):
    city = chr(ord(first_city) + nc)
    cities.update(city)

print(cities)

roads = list()
List_city = tuple(cities)
for nr in range(0,num_road):
    city_road_from , city_road_to = random.sample(List_city,2)
    distance = random.randint(0,100)
    road = {'From' : city_road_from , 'To' : city_road_to , 'Distance' : distance}
    roads.append(road)

print(roads)

print("--------------------------")

#4

def check_round_trip(roads) :
    nroad = len(roads)
    result = set()
    for i in range(0,nroad) :
        cfrom = roads[i]['From']
        cto = roads[i]['To']
        i_min = min(cfrom,cto)
        i_max = max(cfrom,cto)
        for j in range(i+1,nroad) :
            cfrom = roads[j]['From']
            cto = roads[j]['To']
            j_min = min(cfrom,cto)
            j_max = max(cfrom,cto)
            if (i_min == j_min) and (i_max == j_max):
                result.update([i_min + "-" + i_max])
    return result

result = check_round_trip(roads)
if len(result) > 0 :
    print("Found : {}".format(result))
else :
    print("No round-trip route")



    
