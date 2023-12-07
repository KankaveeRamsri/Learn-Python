def fibonacci_sequence(n) : 
    fibonacci = [0,1]
    for i in range(2,n+1) : 
        next_number = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_number)
    
    return fibonacci 

a_number = int(input("Input number of Fibonacci number: "))
answer = fibonacci_sequence(a_number)

result = ""
for i in range(len(answer)) : 
    result += str(answer[i])
    if i != len(answer) - 1 :
        result += ", "

print(result)

print("------------------------------")

def fibonacci(n): # recursive function
    if n == 1 :
        return 1
    elif n == 0 :
        return 0
    else :
        return fibonacci(n-1) + fibonacci(n-2)

a_number = int(input("Input number of Fibonacci number: "))
fibo_sequence = [str(fibonacci(_)) for _ in range(a_number + 1)]
result = ", ".join(fibo_sequence)
print(result)

print("------------------------------")


    

