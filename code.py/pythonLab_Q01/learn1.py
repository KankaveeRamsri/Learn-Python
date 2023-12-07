#1

data = []
for i in range(1,4) :
    name = input(f"Enter name {i}: ")
    data.append(name)
    group = input(f"Enter Group {i}: ")
    data.append(group)
    gpa = input(f"Enter GPA {i}: ")
    data.append(gpa)
print(data)

print("\nReport")
print("-----------------------------------")
print("Name           Group     GPA")
print("-----------------------------------")
print("{:16} {:7} {}".format(data[0],data[1],data[2]))
print("{:16} {:7} {}".format(data[3],data[4],data[5]))
print("{:16} {:7} {}".format(data[6],data[7],data[8]))


print(" ---------------------------- ")

#2

date = input("Enter date : ")

year = int(date) // 10000
day = int(date) % 100
month = int(date[4:6])


if len(date) != 8 :
    print("Error")

elif day <= 9 and month <= 9 :
    print("0{}-0{}-{:4d}".format(day,month,year))

elif day >= 1 and day <= 9 :
    print("0{}-{:2d}-{:4d}".format(day,month,year))

elif month >= 1 and month <= 9 :
    print("{:2d}-0{}-{:4d}".format(day,month,year))

else :
    print("{:2d}-{:2d}-{:4d}".format(day,month,year))

# print(" ---------------------------- ")

#3

# c_year = int(input("Enter current year : "))
# birthyear = int(input("Enter your birth year: "))
# weight = float(input("Enter your weight(kg) : "))
# height_cm = float(input("Enter your height(cm) : "))

# height_m = height_cm / 100

# BMI = weight / pow(height_m,2)
# age = c_year - birthyear
# BMR_m = 66 + (13.75 * weight) + (5 * height_cm) - (6.8 * age)
# BMR_fm = 655 + (9.6 * weight) + (1.8 * height_cm) - (4.7 * age)

# print("---------------")
# print(f"Your age = {age}")
# print("Your BMI = {:.3f}".format(BMI))
# print("Your BMR(male) = {:.3f}".format(BMR_m))
# print("Your BMR(female) = {:.3f}".format(BMR_fm))