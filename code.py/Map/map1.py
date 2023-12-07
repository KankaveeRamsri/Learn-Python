roads = [
            {'From':'A','To':'B','Distance':7},
            {'From':'A','To':'C','Distance':12},
            {'From':'B','To':'C','Distance':10},
            {'From':'B','To':'D','Distance':15}
        ]


def cityList(roads) :
    cities = set()
    for road in roads :
        cities.update(road['From'],road['To'])
    return cities

cities = cityList(roads)
# print(cities)

print("--------------------------")

def roads_from(roads,city):
    data_road = list()
    for road in roads :
        if road['From'] == city :
            data_road.append(road)
    return data_road

result = roads_from(roads , 'A')
# print(result)

print("--------------------------")

import random
import csv

num_city = int(input("Enter num of city : "))
num_road = int(input("Enter num of road : "))
first_city = 'A'
cities = set()
for nc in range(0,num_city) :
    city = (chr(ord(first_city) + nc))
    cities.update(city)

print(cities)

roads = []
List_cities = tuple(cities)
for nr in range(0,num_road) :
    rand_cities_from , rand_cities_to = random.sample(List_cities,2)
    distance = random.randint(1,100)
    road = {'From' : rand_cities_from , 'To' : rand_cities_to , 'Distance' : distance}
    roads.append(road)
print(roads)

with open('roads.csv' , 'w' , newline = '') as csvfile :
    column_names = ['From','To','Distance']
    writer = csv.DictWriter(csvfile,fieldnames = column_names)
    writer.writeheader()
    writer.writerows(roads)

print("--------------------------")

def check_round_tip(roads):
    nroad = len(roads)
    result = set()
    for i in range(0,nroad) : #เช็คเส้นทางแรก
        cfrom = roads[i]['From']
        cto = roads[i]['To']
        i_min = min(cfrom,cto) #เลือกค่าน้อยที่สุดจาก 2 พารามิเตอร์
        i_max = max(cfrom,cto)
        for j in range(i+1 , nroad): #ไปเช็คเส้นทางอื่น ที่ไม่ใช่เส้นทางแรก
            cfrom = roads[j]['From']
            cto = roads[j]['To']
            j_min = min(cfrom,cto)
            j_max = max(cfrom,cto)
            if (i_min == j_min) and (i_max == j_max): #ทุกกรณีถือว่าซ้ำหมด
                result.update([i_min + '-' + i_max])
    return result 

result = check_round_tip(roads)
print(result)
if len(result) > 0 :
    print('Found :' ,result )
else :
    print('No round-tip route')







    
