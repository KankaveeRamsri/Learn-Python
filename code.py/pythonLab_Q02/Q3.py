print("Enter grade ( A -E ) for each course")

print("Physics I")
grade_1 = input("grade : ")
section_1 = int(input("Section : "))
credit_1 = int(input("Credit : "))

print("Math I")
grade_2 = input("grade : ")
section_2 = int(input("Section : "))
credit_2 = int(input("Credit : "))

print("Chemistry")
grade_3 = input("grade : ")
section_3 = int(input("Section : "))
credit_3 = int(input("Credit : "))

print("Intro to Computer : ")
grade_4 = input("grade : ")
section_4 = int(input("Section : "))
credit_4 = int(input("Credit : "))

print("Table tennis")
grade_5 = input("grade : ")
section_5 = int(input("Section : "))
credit_5 = int(input("Credit : "))

def GPA(grade) :
    if grade == 'A'  :
        return 4
    
    elif grade == 'B+'  :
        return 3.5
    
    elif grade == 'B'  :
        return 3
    
    elif grade == 'C+' :
        return 2.5
    
    elif grade == 'C'  :
        return 2
    
    elif grade == 'D+' :
        return 1.5
    
    elif grade == 'D' :
        return 1
    
    elif grade == 'E' :
        return 0
    


print("\n   GRADE REPORT")
print("--------------------------------------------------------------------")
print("#      Course               Section        Credit        Grade ")
print("--------------------------------------------------------------------")


if section_1 < 10 :
    print("{:6}{:24}{:16}{:13}{}".format("1","Physics I",f"0{section_1}",f"{credit_1}",grade_1))
else :
    print("{:6}{:24}{:16}{:13}{}".format("1","Physics I",f"{section_1}",f"{credit_1}",grade_1))

if section_2 < 10 :
    print("{:6}{:24}{:16}{:13}{}".format("2","Math I",f"0{section_2}",f"{credit_2}",grade_2))
else :
    print("{:6}{:24}{:16}{:13}{}".format("2","Math I",f"{section_2}",f"{credit_2}",grade_2))

if section_3 < 10 :
    print("{:6}{:24}{:16}{:13}{}".format("3","Chemistry",f"0{section_3}",f"{credit_3}",grade_3))
else :
    print("{:6}{:24}{:16}{:13}{}".format("3","Chemistry",f"{section_3}",f"{credit_3}",grade_3))

if section_4 < 10 :
    print("{:6}{:24}{:16}{:13}{}".format("4","Intro to Computer",f"0{section_4}",f"{credit_4}",grade_4))
else :
    print("{:6}{:24}{:16}{:13}{}".format("4","Intro to Computer",f"{section_4}",f"{credit_4}",grade_4))

if section_5 < 10 :
    print("{:6}{:24}{:16}{:13}{}".format("5","Table tennis",f"0{section_5}",f"{credit_5}",grade_5))
else :
    print("{:6}{:24}{:16}{:13}{}".format("5","Table tennis",f"{section_5}",f"{credit_5}",grade_5))

print("--------------------------------------------------------------------")

result_1 = GPA(grade_1) * credit_1
result_2 = GPA(grade_2) * credit_2
result_3 = GPA(grade_3) * credit_3
result_4 = GPA(grade_4) * credit_4
result_5 = GPA(grade_5) * credit_5
sum_gpa = (result_1 + result_2 + result_3 + result_4 + result_5) / (credit_1 + credit_2 + credit_3 + credit_4 +credit_5)

print("\n      GPA = {:.2f}".format(sum_gpa))
print("---------------------")











