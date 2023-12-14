# Method 1

# def swap_case(s) :
#     text_swap = ""
#     for i in s :
#         if i.islower():
#             text_swap += i.upper()
#         elif i.isupper():
#             text_swap += i.lower()
#         else:
#             text_swap += i
    
#     return text_swap

# if __name__ == "__main__" :
#     s = input()
#     result = swap_case(s)
#     print(result)            
    
print("-----------------------------------")

# Method 2 

def swap_case(s):
    return s.swapcase()

if __name__ == "__main__" :
    s = input()
    result = swap_case(s)
    print(result)  
