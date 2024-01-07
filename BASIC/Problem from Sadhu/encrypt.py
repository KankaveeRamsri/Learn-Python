import string 

while True : 
    user_input = input("Enter 5 characters: ").upper()
    if len(user_input) != 5 :
        pass
    else : 
        break
    
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase[::-1] 

alphabet1 = uppercase.index(user_input[0])


def encoder() :
    answer = ""
    for i in range(5) :
        alphabet = uppercase.index(user_input[i])
        answer += lowercase[alphabet]
    return answer

result = encoder()
print("Encryption is {}".format(result))