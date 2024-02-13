def count_number(str1):
    count = 1 
    str2 = ""

    for i in range(len(str1)) :
        if i != len(str1) - 1 :
            if str1[i] == str1[i+1] :
                count += 1 
            
            else :
                str2 += "({}, {}) ".format(str(count), str1[i])
                count = 1

        
        elif i == len(str1) - 1 :
            str2 += "({}, {}) ".format(str(count), str1[i])
            
    return str2


if __name__ == "__main__":
    string = input("Enter String: ")
    print(count_number(string))
    
    