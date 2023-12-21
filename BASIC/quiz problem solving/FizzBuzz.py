# summation = 0
# num_list = []

# print("Welcome to FizzBuzz Game")
# while True :
#     num = int(input("Enter number: "))
#     if num % 3 == 0 and num % 5 == 0 :
#         convert = 'FizzBuzz'
#     elif num % 3 == 0 :
#         convert = 'Fizz'
#     elif num % 5 == 0 :
#         convert = 'Buzz'
#     else :
#         convert = 'NoFizzBuzz'
    
#     modulo = num % len(convert)
#     summation += modulo
#     num_list.append(num)
    
#     if summation > 20 :
#         break
    
# answer = summation % num_list[-1]
# print("Your score: {}".format(answer))

print("-----------------------------------")

# Method ( P'Boat )

def get_fizz_buzz(number:int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    
    return "NoFizzBuzz"

if __name__ == '__main__':
    counter:int = 0
    number:int = 0
    print('Welcome to FizzBuzz Game')
    while counter <= 20:
        number = int(input('Enter number: '))
        word = get_fizz_buzz(number)
        counter += number % len(word)
        
    print("Your score:",counter % number)
    
    





    
        
    
    