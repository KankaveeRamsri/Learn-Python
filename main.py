# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = [float(x) for x in line]
#         student_marks[name] = scores
#     query_name = input()
    
#     for key, value in student_marks.items():
#         if key == query_name :
#             values = sum(value) / len(value)
#             print('{:.2f}'.format(values))

print("------------------------------------")

import string

if __name__ == '__main__':
    alphabet_dict = {}
    
    lowercase = string.ascii_lowercase
    print(lowercase)
    
    s = str(input()).lower()
    s = s.replace(" ","")
    
    for i in lowercase:
        alphabet_dict[i] = lowercase.count(i)
    
    for string in s:
        alphabet_dict[string] += 1 
    
    if any(value == 1 for value in alphabet_dict.values()):
        print(False)
    
    
             
    
    
    