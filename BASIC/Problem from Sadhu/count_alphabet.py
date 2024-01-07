# import string
# lower_alpha = {}

# while  True :
#     user = input("Enter string: ")
#     if user == "end" :
#         break
#     user = user.lower()
#     for s in user :
#         if s in string.ascii_lowercase: 
#             if s in lower_alpha.keys(): 
#                 lower_alpha[s] +=1  
#             else :
#                 lower_alpha[s] = 1

# print(lower_alpha)
# lower_alpha_sorted = dict(sorted(lower_alpha.items()))
# print(lower_alpha_sorted)
# print('*'*30)
# print('*',' '*3,'Alphabet Counting',' '*4,'*')
# print('*'*30)

# for key, value in lower_alpha_sorted.items():
#     print(key, value)

# print('*'*30)






import string 
lower_alpha = {}

while True :
    text = input("Enter string : ")   
    text = text.lower()
    if text == 'end' :
        break 
    else :
        for i in text : 
            if i in string.ascii_lowercase :
                if i in lower_alpha.keys() :
                    lower_alpha[i] += 1
                else :
                    lower_alpha[i] = 1

print(dict(sorted(lower_alpha.items())))


