data = []
for i in range(1,4) :
    name = input(f"Enter name {i}: ")
    data.append(name)
    group = input(f"Enter Group {i}: ")
    data.append(group)
    gpa = input(f"Enter GPA {i}: ")
    data.append(gpa)

print("\nReport")
print("-----------------------------------")
print("Name           Group     GPA")
print("-----------------------------------")
print("{:16} {:7} {}".format(data[0],data[1],data[2]))
print("{:16} {:7} {}".format(data[3],data[4],data[5]))
print("{:16} {:7} {}".format(data[6],data[7],data[8]))