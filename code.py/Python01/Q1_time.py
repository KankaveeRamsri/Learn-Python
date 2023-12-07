import random
import time
lower = -100
upper = 100
# n = 100
data_num = []
position_max_number = []
position_min_number = []
for n in range(100,1100,100):
    print("--------- (n = {}) ---------".format(n))
    for i in range(0,n):
        rand_num = random.randint(lower,upper)
        data_num.append(rand_num)

    for i in range(0,n):
        if data_num[i] == max(data_num) :
            position_max_number.append(i) 
        if data_num[i] == min(data_num) :
            position_min_number.append(i)
    print('-'*30)
    # print("Maximum number # {} is {}".format(n,max(data_num)))
    # print("Minimum number # {} is {}".format(n,min(data_num)))
    

    avg_time_max = []
    for i in range(0,10) :
        startTime = time.perf_counter_ns()
        val = max(data_num)
        endTime = time.perf_counter_ns()
        avg_time_max.append(endTime - startTime)

    print("Process time to find maximum number #{} : {}".format(n,sum(avg_time_max) / 10))

    # print('-'*30)

    avg_time_min = []
    for i in range(0,10) :
        startTime = time.perf_counter_ns()
        val2 = min(data_num)
        endTime = time.perf_counter_ns()
        avg_time_min.append(endTime - startTime)

    print("Process time to find minimum number #{} : {}".format(n,sum(avg_time_min) / 10))
    print('-'*30)


        
