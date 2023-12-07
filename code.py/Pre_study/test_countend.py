import string
lower_alpha = {}

while  True :
    user = input("Enter your word : ")
    if user == "end" :
        break
    user = user.lower()
    for s in user :
        if s in string.ascii_lowercase: 
            if s in lower_alpha.keys(): #เช็คว่ามีอยู่ในคีย์ยัง
                lower_alpha[s] +=1  #ถ้ามีแล้วบวกต่อไปเลย
            else :
                lower_alpha[s] = 1 #ถ้ายังไม่มี เพิ่มเข้ามาใหม่ 
                
    # print(lower_alpha)
print(lower_alpha)

list_values = list()
for i in lower_alpha.values() :
    list_values.append(i)
    
for i in range(len(lower_alpha)) :
    print(list(lower_alpha.keys())[i],end=" ")
    print(list_values[i])
    
