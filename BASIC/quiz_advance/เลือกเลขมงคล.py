if __name__ == '__main__':
    a_number = int(input())
    a_number_of_factors = []
    for i in range(a_number):
        ls_factor = []
        number = int(input())
        for j in range(1,number + 1):
            if number % j == 0:
                ls_factor.append(j)   
        a_number_of_factors.append(len(ls_factor))
        ls_factor = []
    
    answer = []
    for x in a_number_of_factors: 
        if x % 2 == 0:
            answer.append('NO')
        else:
            answer.append('YES')
    
    for _ in answer:
        print(_)

            