if __name__ == '__main__':
    a_number = int(input())
    ls_count = []
    for _ in range(a_number):
        ls_number = []
        number = int(input())
        for i in range(1,number+1):
            if number % i == 0:
                ls_number.append(i)
        
        count = 0
        for j in str(number):
            if int(j) in ls_number:
                count += 1
        ls_count.append(count)
        count = 0
    
    for x in ls_count:
        print(x)
        
