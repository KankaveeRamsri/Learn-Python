def is_Fizz_Buzz(numbers):
    
    for num in numbers:
        if num % 15 == 0 :
            print("FizzBuzz")
        elif num % 3 == 0 :
            print("Fizz")
        elif num % 5 == 0 :
            print("Buzz")
        else :
            return False
