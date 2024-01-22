# Method I (ผิด 1 กรณี)

if __name__ == "__main__":
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    dict_bird = {}
    for count in arr:
        if count in dict_bird.keys():
            dict_bird[count] += 1 
        else:
            dict_bird[count] = 1
    
    max_count = -1
    max_key = None

    for key, value in dict_bird.items():
        if value > max_count:
            max_count = value
            max_key = key

    print(max_key)
    
print("---------------------------------------")

# Method II (ถูกหมด)

# if __name__ == "__main__":
#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))
    
#     counter = [0, 0, 0, 0, 0]
#     for i in arr:
#         counter[i-1] += 1
        
#     print(counter)
    
#     print((counter.index(max(counter)))+1)
    