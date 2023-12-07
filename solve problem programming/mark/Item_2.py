# Item 2 ( My solution )

# user_1 = input().split() # year month day 
# user_2 = input().split() # year month day 

# if user_1[0] < user_2[0] :
#     print("1")
# elif user_1[0] > user_2[0] :
#     print("2")
# elif user_1[0] == user_2[0] :
#     if user_1[1] < user_2[1] :
#         print("1")
#     elif user_1[1] > user_2[1] :
#         print("2")
#     elif user_1[1] == user_2[1] :
#         if user_1[2] < user_2[2] :
#             print("1")
#         elif user_1[2] > user_2[2] :
#             print("2")
#         elif user_1[2] == user_2[2] :
#             print("equal")


print("----------------------")

# Item 2 ( Mark's Solution )

y1 , m1 , d1 = [int(e) for e in input().split()] # pattern ในการรับอินพุตหลายตัวในบรรทัดเดียว
y2 , m2 , d2 = [int(e) for e in input().split()]

if y1 < y2 :
    print("1")
elif y1 > y2 :
    print("2")
elif y1 == y2 : 
    if m1 < m2 :
        print("1")
    elif m1 > m2 :
        print("2")
    elif m1 == m2 :
        if d1 < d2 :
            print("1")
        elif d2 < d1 :
            print("2")
        elif d1 == d2 :
            print("equal")



