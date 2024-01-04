def get_Fizz_Buzz(num):
    
    if num % 15 == 0 :
        return "FizzBuzz"
    elif num % 3 == 0 :
        return "Fizz"
    elif num % 5 == 0 :
        return "Buzz"
    return ""


print(get_Fizz_Buzz(3))
    