n = int(input('Enter number: '))

base2 = ''
base10 = n

while base10 > 0 :
    frac = int(base10 % 2)
    base2 = str(frac) + base2
    base10 = (base10 - frac)/2

print('{} is {} in base 2.'.format(n,base2))