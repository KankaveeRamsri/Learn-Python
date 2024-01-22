# if __name__ == '__main__':
#     print("Fireworks Counter")
#     scores = dict()
#     while (data := input("Enter color code: ")) != "END":
#         for i, a in enumerate(data):
#             if a.isdigit():
#                 break
        
#         key = "".join(sorted(data[:i]))
#         if key not in scores:
#             scores[key] = 0
#         scores[key] += int(data[i:])
#         print(f"{key:5} -> {scores[key]:10}")
#         # print(scores.items())
        
#     display_key = sorted(scores.keys())
#     print()
#     print("Fireworks Statistic")
#     for key in display_key:
#         print(f"{key:5} -> {scores[key]:10}")

print("--------------------------------------")

# print("Fireworks Counter")
# scores = {}

# while True:
#     data = input("Enter color code: ")
#     if data == "END":
#         break

#     color_code = ""
#     number = ""

#     # แยกตัวอักษรและตัวเลข
#     for char in data:
#         if char.isdigit():
#             number += char
#         else:
#             color_code += char

#     # ข้ามการนับถ้าไม่มีตัวเลข
#     if not number:
#         continue

#     number = int(number)
#     sorted_color_code = ''.join(sorted(color_code))
#     scores[sorted_color_code] = scores.get(sorted_color_code, 0) + number

#     # แสดงคะแนนสำหรับสีปัจจุบัน
#     print(f"{sorted_color_code:5} -> {scores[sorted_color_code]:10}")
#     print(scores)

# print("\nFireworks Statistic")
# for key in sorted(scores.keys()):
#     print(f"{key:5} -> {scores[key]:10}")

print("--------------------------------------")

print("Fireworks Counter")

scores = dict()
while (data := (input("Enter color code: ")).upper()) != 'END':
    
    color_code = ""
    number = ""
    
    for char in data:
        if char.isdigit():
            number += char
        else:
            color_code += char
    
    # print(color_code)
    # print(number)
    
    if not number:
        continue
    
    number = int(number)
    sorted_color_code = "".join(sorted(color_code))
    scores[sorted_color_code] = scores.get(sorted_color_code, 0) + number
    
    print(f"{sorted_color_code:<5} -> {scores[sorted_color_code]:5}")
    # print(scores)

print("\nFireworks Statistic")    
for key, values in scores.items():
    print(f"{key:5} -> {values:10}")
    
    
    
    
    
    




