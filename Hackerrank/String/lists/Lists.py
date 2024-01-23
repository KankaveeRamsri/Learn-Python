if __name__ == '__main__':
    N = int(input("N = "))
    my_list = []
    
    for i in range(N) :
        list_input = input().split()
        
        method = list_input[0]
        
        if method == "insert":
            my_list.insert(int(list_input[1]),int(list_input[2]))
        elif method == "append":
            my_list.append(int(list_input[1]))
        elif method == "remove":
            my_list.remove(int(list_input[1]))
        elif method == "print":
            print(my_list)
        elif method == "sort":
            my_list.sort()
        elif method == "pop":
            my_list.pop()
        elif method == "reverse":
            my_list.reverse()

