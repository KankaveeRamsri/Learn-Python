# token = str(input("Enter Token number: "))


# a_number_of_ackara = int(len(token)) 

# summation_of_1 = 0 
# for i in token :
#     summation_of_1 += int(i)

# a_number_of_zero = 0 
# for i in token :
#     if int(i) == 0 :
#         a_number_of_zero += 1


# if '2' in token or '3' in token or '4' in token or '5' in token or '6' in token or '7' in token or '8' in token or '9' in token :      
#     print("Your token is invalid")

# else :
#     if a_number_of_ackara % summation_of_1 == a_number_of_zero :
#         print("You get jackpot!!")
#     else :
#         print("See you next time, have a nice day.")

print("-----------------------------------------------------")

token = input("Enter Token number : ")
a = token.count('1')
b = token.count('0')

def is_binary_number(number) : 
    for digit in number :
        if digit != '0' and digit != '1' :
            return False
        
    return True 

if is_binary_number(token) :
    if len(token) % a == b :
        print("You get jackpot!!")
        
    else :
        print("See you next time, have a nice day.")
else :
    print("Your token is invalid")
    


    

        
    

    