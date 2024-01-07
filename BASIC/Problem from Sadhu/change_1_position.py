import string

def check_len_text(prompt) :
    while True :
        try : 
            value = str(input(prompt))
            if len(value) == 3 :
                return value
            else :
                print("Error!,text must be 3 alphabets")
        except ValueError :
            break


text = check_len_text("Enter 3 characters: ").upper()

uppercase = string.ascii_uppercase
new_value = "BCDEFGHIJKLMNOPQRSTUVWXYZA"

result = ""
for i in range(3) :
    alphabet = uppercase.index(text[i])
    result += new_value[alphabet]

print("Ciphertext is {}".format(result))