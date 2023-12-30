number_word = int(input("Word = "))

dict_ans = {}

for i in range(number_word):
    word = input(">>> ")
    if word in dict_ans.keys():
        dict_ans[word] += 1 
    else :
        dict_ans[word] = 1

print("Ans =>")
print(len(list(dict_ans.keys())))

for key, value in dict_ans.items():
    print(value,end=" ")


    