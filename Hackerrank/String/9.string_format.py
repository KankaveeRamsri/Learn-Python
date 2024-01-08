def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        decimal_format = "{:>{width}}".format(i, width=width)
        octal_format = "{:>{width}}".format(oct(i).replace("0o",""), width=width)
        hexadecimal_format = "{:>{width}}".format((hex(i).replace("0x","")).upper(), width=width)
        binary_format = "{:>{width}}".format(bin(i).replace("0b",""), width=width)
        
        print("{} {} {} {}".format(decimal_format, octal_format, hexadecimal_format, binary_format))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


