text_input = str(input("Enter value in mm, cm, and m: " ))
unit = str(input("Enter unit to convert in mm, cm, m: "))

if 'mm' in text_input and unit == 'm' :
    value = float(text_input.replace('mm',"")) / 1000
    print("Value after unit conversion is {}m".format(value))

elif 'mm' in text_input and unit == 'cm' :
    value = float(text_input.replace('mm',"")) / 10
    print("Value after unit conversion is {}cm".format(value))

elif 'mm' in text_input and unit == 'mm' :
    value = float(text_input.replace('mm',''))
    print("Value after unit conversion is {}mm".format(value))

elif 'cm' in text_input and unit == 'm' :
    value = float(text_input.replace('cm',"")) / 100
    print("Value after unit conversion is {}m".format(value))

elif 'cm' in text_input and unit == 'mm': 
    value = float(text_input.replace('cm','')) * 10
    print("Value after unit conversion is {}mm".format(value))

elif 'cm' in text_input and unit == 'cm' :
    value = float(text_input.replace('cm',''))
    print("Value after unit conversion is {}cm".format(value))

elif 'm' in text_input and unit == 'mm' :
    value = float(text_input.replace('m','')) * 1000
    print("Value after unit conversion is {}mm".format(value))

elif 'm' in text_input and unit == 'cm':
    value = float(text_input.replace('m','')) * 100
    print("Value after unit conversion is {}cm".format(value))

elif 'm' in text_input and unit == 'm' : 
    value = float(text_input.replace('m',''))
    print("Value after unit conversion is {}m".format(value))