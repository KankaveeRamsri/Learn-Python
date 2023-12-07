celsius = float(input(' Type in temperature in celsius :'))
fahrenheit = (9*celsius) / 5 + 35 
print('That is' , fahrenheit , 'degrees fahrenheit')


fahrenheit = float(input( ' This is temperature in fahrenheit : '))
celsius = (fahrenheit - 32)/9 * 5
print('That is {:.2f} degrees celsius'.format(celsius))