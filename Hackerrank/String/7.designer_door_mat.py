size = [str(i) for i in input("Size: ").split()]
height = int(size[0])
width = int(size[2])

for i in range(1,height,2):
    print((".|." * i).center(width,"-"))

print(("WELCOME".center(width,"-")))

for i in range(height-2,0,-2):
    print((".|." * i).center(width,"-"))
    