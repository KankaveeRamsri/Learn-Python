# def countdown(n) : 
#     print(n)
#     if n == 0 :
#         return
#     else :
#         countdown(n-1)

# countdown(5)

print("------------------------------")

# Palindromes ( no recursive function )

# app 1 :

# def is_palindrome(word:str) -> bool :
#     return word == word[::-1]

# if __name__ == "__main__" :
#     for word in ['level','civic'] :
#         print(word, is_palindrome(word))
        

# How to use zip and enumerate :

# x = [0,1,2]
# y = [9,8,7]

# for i,j in zip(x,y) :
#     print(i,j)

print("------------------------------")

# for i,j in enumerate(y) :
#     print(i,j)

print("------------------------------")

# Palindromes ( use recursive function )

# def check_palindrome(word) :
#     if len(word) <= 1 :
#         return True
    
#     if word[0] == word[-1] :
#         return check_palindrome(word[1:-1])
    
#     else :
#         False

# text = str(input())
# if check_palindrome(text) :
#     print(f"{text} is a palindrome.")
# else :
#     print(f"{text} is not a palindrome.")

print("------------------------------")

def list_num(num_list) :
    the_sum = 0
    for i in num_list :
        the_sum += i
    
    return the_sum

print(list_num([1,3,5,7,9]))

print("------------------------------")

def list_sum(num_list) :
    if len(num_list) == 1 : # การตรวจสอบนี้สำคัญมากเพราะจะทำให้เราออกจากฟังก์ชันได้
        return num_list[0]
    
    else : # recursive function 
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1,3,5,7,9]))

print("------------------------------")

# def fac(n) :
#     if n == 0 :
#         return 1 
#     else :
#         return n * fac(n-1)

# n = 5
# print("{}! = {}".format(n,fac(n)))

print("------------------------------")

# def fibonacci(n) :
#     if n == 1 :
#         return 0 
#     elif n == 2 :
#         return 1 
#     else : 
#         return fibonacci(n-2) + fibonacci(n-1)

# n = 8 
# print("Fibonacci sequence at position {} is {}".format(n,fibonacci(n)))
    
print("------------------------------")

import datetime

def power(base,exponent) : # Recursive function 
    if exponent == 0 :
        return 1
    else :
        return base * power(base,exponent - 1)

print(power(10,12))

print("----------------")

