import string
x = string.ascii_lowercase

n = 3
for i in range(n):

    letters = "-".join((x[n-1 - j]) for j in range(i + 1))
    line = letters + letters[-2::-1] 

    print(line.center(4*n-3, "-")) # สูตรได้มาจากคิดสมการอนุกรม

for i in range(n-2, -1, -1):

    letters = "-".join((x[n-1 - j]) for j in range(i + 1))
    line = letters + letters[-2::-1] 

    print(line.center(4*n-3, "-"))

