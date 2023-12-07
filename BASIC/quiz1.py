number = int(input("Enter computer status code: "))

number = number // 10
number = number % 3

if number == 0 :
    print("Complete")

elif number == 1 :
    print("Waiting")

elif number == 2 :
    print("Error")