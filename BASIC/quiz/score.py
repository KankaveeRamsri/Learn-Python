def get_grade(score):
    if score >= average_xi + (2*sd) :
        return 'A'
    elif score >= average_xi + sd :
        return 'B'
    elif score > average_xi - sd and score < average_xi + sd :
        return 'C'
    elif score <= average_xi - sd :
        return 'D'
    else :
        return 'F'

def get_average_xi(xi) :
    return sum(xi) / len(xi)

def calculate_sd():
    si = 0 
    for x in xi :
        si += pow((x - average_xi) , 2) 

    sd = pow((si / (len(xi) - 1)) , 0.5)
    
    return sd    

if __name__ == '__main__' :
    xi = [int(_) for _ in input("All score : ").split()]
    student_score = float(input("student score : ")) 
    
    average_xi = get_average_xi(xi)
    sd = calculate_sd()
    
    output = get_grade(student_score)
    print(output)
    

    





