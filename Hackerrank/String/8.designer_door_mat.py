# if __name__ == "__main__":
#     size = input("Size: ")
#     dimension = size.split(" x ")
    
#     height = int(dimension[0])
#     width = int(dimension[1])
    
#     for i in range(1, height, 2):
#         print((".|." * i).center(width,"-"))
    
#     print("WELCOME".center(width,"-"))
    
#     for i in range(height-2,0,-2):
#         print((".|." * i).center(width,"-"))

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

print(list(squared))
