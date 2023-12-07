# Item 7 ( My solution )

number = [int(i) for i in input().split()]

if number[0] > number[1] > number[2]:
    print("decreasing")

elif number[0] < number[1] < number[2]:
    print("increasing")

else:
    print("neither")

print("----------------------")

# Item 7 ( Mark's solution)