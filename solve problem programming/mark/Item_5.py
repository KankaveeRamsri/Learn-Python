# Item 5 ( My Solution )

# number = int(input())

# if number <= 0 : 
#     print("Error : Please input positive number")
# elif number >= 10 :
#     print("Error : Out of range")
# else : 
#     if number == 1 or number == 2 or number == 3 :
#         result = ""
#         for i in range(number) :
#             result += "I"
#         print(result)

#     elif number == 4 :
#         print("IV")

#     elif number == 5 :
#         print("V")

#     elif number == 6 or number == 7 or number == 8 : 
#         result = "V"
#         for i in range(number - 5) :
#             result += "I"
#         print(result)

#     elif number == 9 :
#         print("IX")

print("----------------------")

# Item 5 ( Mark's Solution )

n = int(input())
num1 = ["I","II","III","IV","V","VI","VII","VIII","IX"]

if n < 0 : 
    print("Error : Please input positive number")

elif n == 0 or n > 9 :
    print("Error : Out of range")

else : 
    print(num1[n-1])

print("----------------------")

