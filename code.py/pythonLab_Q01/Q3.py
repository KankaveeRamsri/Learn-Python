c_year = int(input("Enter current year : "))
birthyear = int(input("Enter your birth year: "))
weight = float(input("Enter your weight(kg) : "))
height_cm = float(input("Enter your height(cm) : "))

height_m = height_cm / 100

BMI = weight / pow(height_m,2)
age = c_year - birthyear
BMR_m = 66 + (13.75 * weight) + (5 * height_cm) - (6.8 * age)
BMR_fm = 655 + (9.6 * weight) + (1.8 * height_cm) - (4.7 * age)

print("---------------")
print(f"Your age = {age}")
print("Your BMI = {:.3f}".format(BMI))
print("Your BMR(male) = {:.3f}".format(BMR_m))
print("Your BMR(female) = {:.3f}".format(BMR_fm))