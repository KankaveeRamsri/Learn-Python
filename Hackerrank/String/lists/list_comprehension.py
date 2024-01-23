if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    ArrayList = []
    for x in range(x+1):
        for y in range(y+1):
            for z in range(z+1):
                ArrayList.append([x,y,z])
    
    
    discard_list = [x for x in ArrayList if sum(x) == n]
    for x in discard_list:
        ArrayList.remove(x)
    
    print(ArrayList)