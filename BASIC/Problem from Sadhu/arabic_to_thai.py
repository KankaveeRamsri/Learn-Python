def get_number(prompt) :
    while True : 
        try : 
            value = input(prompt)
            if len(str(value)) == 5 :
                return str(value)
            else :
                print("Error, Value must be 5 units.")

        except ValueError :
            print("Error, Value must be integer number.")


arabic_input = get_number("Enter only 5 Arabic number: ")
arabic_num = '1234567890'
thai_num = '๑๒๓๔๕๖๗๘๙๐'

result = ''
for i in range(5) : 
    num = arabic_num.index(arabic_input[i])
    result += thai_num[num]

print("Thai number is {}".format(result))