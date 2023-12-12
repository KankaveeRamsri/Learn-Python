def check_path(path):
    Location =[]
    mylist = [0,0]
    
    for i in path :
        if i == '>' :
            mylist[0] += 1 
        elif i == '<' :
            mylist[0] -= 1
        elif i == '^' :
            mylist[1] += 1
        elif i == 'v' :
            mylist[1] -= 1
        elif i == 'x' :
            Location.append(tuple(mylist[:]))
            

    return Location

if __name__ == '__main__':
    path = str(input("Path: "))
    all_path = check_path(path)
    if 'x' not in path:
        print("Not Found")
    else :
        print("Locations:"," ".join(str(i) for i in all_path))


    
    
    
    
    
    
