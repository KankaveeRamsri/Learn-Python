# import datetime as dt

# def first_n(n) : # วิธีปกติ
#     num , nums = 0 , []
#     while num < n :
#         nums.append(num)
#         num += 1 
#     return nums 

# start_time = dt.datetime.now()

# data = first_n(1_000_000)
# stop_gen_time = dt.datetime.now()
# sum_of_first_n = sum(data)
# stop_time = dt.datetime.now()

# print('time gen {}'.format(stop_gen_time - start_time))
# print('time sum {}'.format(stop_time - start_time))

print("-------------------------------------------")

# class first_n(object) : # ทำให้เป็น generator # ไม่นิยมใช้ เป็นวิธีที่ยาก
#     def __init__(self,n) :
#         self.n = n
#         self.num = 0
    
#     def __iter__(self) :
#         return self

#     # Python 3 compatibility
#     def __next__(self) :
#         return self.next()
    
#     def next(self) :
#         if self.num < self.n :
#             cur , self.num = self.num , self.num + 1
#             return cur
#         raise StopIteration

# sum_of_first_n = sum(first_n(1_000_000))

print("-------------------------------------------") 

# def firstn(n) : # นิยมใช้ # ใช้ generator เร็วกว่าครึ่งนึง
#     num = 0
#     while num < n : 
#         yield num
#         num += 1 

# start = dt.datetime.now()
# sum_of_first_n = sum(firstn(1_000_000))
# stop = dt.datetime.now()
# print("data" , sum_of_first_n)
# print("time" , stop - start) 

print("-------------------------------------------") 

# doubles = [2 * n for n in range(50)]
# print(doubles)

# doubles = list(2 * n for n in range(50))
# print(doubles)

print("-------------------------------------------") 
