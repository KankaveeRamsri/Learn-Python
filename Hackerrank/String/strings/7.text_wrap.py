# Method 1

def wrap(string, width):
    new_str = ""
    for i in range(0, len(string), width):
        new_str += string[i:i+width] + "\n"
    return new_str

if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
# Method 2

# def wrap(string, max_width):
#     wrap_str = ""
#     while len(string) > 0:
#         wrap_str += string[:max_width] + "\n"
#         string = string[max_width:]
#     return wrap_str

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)




    