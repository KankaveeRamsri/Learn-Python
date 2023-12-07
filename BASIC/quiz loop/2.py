
# input_i = int(input("Enter number i: "))
# input_j = int(input("Enter number j: "))
# magic_num = int(input("Enter magic number: "))

# num_i = []
# num_j = []

# for i in range(input_i + 1) :
#     num_i.append(i)
# for j in range(input_j + 1) :
#     num_j.append(j)

# answer = []
# for i in num_i :
#     for j in num_j :
#         answer.append(str(i) + str(j))

# result = 0
# for i in answer :
#     if int(i) % magic_num == 0 :
#         result += 1

# print("Found {} magic numbers".format(result))

input_i = int(input("Enter number i: "))
input_j = int(input("Enter number j: "))
magic_num = int(input("Enter magic number: "))
1
# สร้าง List ของตัวเลขทั้งหมดใน input_i และ input_j โดยใช้ List Comprehension
all_numbers = [int(str(x) + str(y)) for x in range(input_i + 1) for y in range(input_j + 1)]

# นับจำนวน magic numbers โดยใช้ฟังก์ชัน sum() และ List Comprehension
result = sum(1 for num in all_numbers if num % magic_num == 0)

print("Found {} magic numbers".format(result))
