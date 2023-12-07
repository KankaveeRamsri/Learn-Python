import random
rand_num = random.randint(0,20)
print(rand_num)

num = int(input('Select number :'))

# if abs(num - rand_num) <= 10 :
#     print('Close')
# elif abs(num - rand_num) > 10 :
#     print('far')
# elif num == rand_num :
#     print('Good job , it\'s equal')
# else : 
#     print('bye')

if num >= 0 and num <=20 :
    if num == rand_num :
        print('Good job , it\'s equal')
    elif abs(num - rand_num) <= 10 :
        print('Close')
    else :
        print('far')
    # elif abs(num - rand_num) > 10 :
    #     print('far')
    
else : 
    print('out of range')      