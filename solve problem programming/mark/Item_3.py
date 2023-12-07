# Item 3 ( My Solution )

def run_length_encoding(s) :
    result = ""
    count = 1 

    for i in range(len(s)) :
        if i != len(s) - 1 :
            if s[i] == s[i + 1] :
                count += 1
        
            elif s[i] != s[i + 1] :
                result += str(count) + s[i]
                count = 1
        
        else : 
            result += str(count) + s[i]

    return result
        
alphabet = str(input()).upper()
answer = run_length_encoding(alphabet)
print(answer)

print("----------------------")

# Item 3 ( Mark's Solution )

# str1 = input().upper()
# count = 1 
# str2 = ""

# for i in range(len(str1)) :
#     if i != len(str1) - 1 :
#         if str1[i] == str1[i+1] :
#             count += 1 
        
#         else :
#             str2 += str(count)
#             str2 += str1[i]
#             count = 1

    
#     elif i == len(str1) - 1 :
#         str2 += str(count)
#         str2 += str1[i]

# print(str2)