import string

print("Select 2 options")
print(" - 1 encrypt with ROT 13")
print(" - 2 decrypt with ROT 13 \n")

option = str(input("Choose option: "))
text = str(input("Enter text: "))

lower_alpha = string.ascii_lowercase
upper_alpha = string.ascii_uppercase

answer = ""

for i in text :
    if i.isupper() :
        if option == '1' :
            answer += upper_alpha[(upper_alpha.index(i) + 13) % 26]
        elif option == '2' :
            answer += upper_alpha[(upper_alpha.index(i) - 13) % 26]
    
    elif i.islower() :
        if option == '1' :
            answer += lower_alpha[(lower_alpha.index(i) + 13) % 26]
        elif option == '2' :
            answer += lower_alpha[(lower_alpha.index(i) - 13) % 26]
    
    else :
        answer += i
    
if option == '1' :
    print('Ciphertext is "{}"'.format(answer))
elif option == '2' :
    print('Plaintext is "{}"'.format(answer))