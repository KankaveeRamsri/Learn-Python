# Item 6 ( My solution )

number = [int(_) for _ in input().split()]

if number[0] == number[1] == number[2]:
    print("all the same")

elif number[0] != number[1] and number[0] != number[2] and number[1] != number[2] :
    print("all different")

else:
    print("neither")

print("----------------------")

# Item  6 ( Mark's solution)

