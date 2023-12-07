import random
import csv

number_of_city = int(input("Enter number of city : "))
number_of_road = int(input("Enter number of road : "))
Firstcity = 'A'
cities = set()

for num_city in range(0,number_of_city):
    city = chr(ord(Firstcity) + num_city)
    cities.update(city)

print(cities)

Listcities = tuple(cities)
roads = list()


for num_road in range(0,number_of_road):
    city_from , city_to = random.sample(Listcities,2)
    rand_distance = random.randint(1,100)
    road = {'From' : city_from , 'To' : city_to , 'Distance' : rand_distance }
    roads.append(road)

print(roads)

with open('road1.csv' , 'w' , newline='') as csvfile :
    column_header = ['From' , 'To' , 'Distance']
    file_writer = csv.DictWriter(csvfile,fieldnames=column_header)
    file_writer.writeheader()
    file_writer.writerows(roads)

def check_round_tip(roads):
    num_roads = len(roads)
    result = set()
    for i in range(0,num_roads):
        cfrom = roads[i]['From']
        cto = roads[i]['To']
        i_min = min(cfrom,cto)
        i_max = max(cfrom,cto)
        for j in range(i+1,num_roads):
            cfrom = roads[j]['From']
            cto = roads[j]['To']
            j_min = min(cfrom,cto)
            j_max = max(cfrom,cto)
            if (i_min == j_min) and (i_max == j_max):
                result.update([i_min + '-' + i_max])
    return result

result = check_round_tip(roads)
if len(result) >= 1 :
    print('Found round tip : {}'.format(result))
else : 
    print('No round-tip route')

# print(roads[0])
# print(roads[0]['From'])

for x in range(0,number_of_road) :
    new_roads = list()
    # print(roads[x])
    if  {'From' : roads[x]['From'] ,'To' : roads[x]['To']} in new_roads :
        continue
    elif  {'From' : roads[x]['To'] ,'To' : roads[x]['From']} in new_roads :
        continue
    new_roads.append(roads[x])
print(new_roads)

# with open('road1.csv','r', newline = '') as csvfile :
#     reader = csv.DictReader(csvfile)
#     for row in reader :
#         new_from = row['From']
#         new_to = row['To']
#         if {'From' : new_from , 'To' : new_to} in new_roads :
#             continue
#         elif {'From' : new_to , 'To' : new_from} in new_roads :
#             continue
#         new_roads.append(row)

# print(new_roads)
    

# with open('new_road1.csv','w',newline='',encoding='utf8') as csvfile :
#     column_new_header = ['From','To','Distance']
#     file_new_writer = csv.DictWriter(csvfile,fieldnames=column_new_header)
#     file_new_writer.writeheader()
#     file_new_writer.writerows(new_roads)


