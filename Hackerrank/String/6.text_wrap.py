def wrap(string, width):
    new_str = ""
    for i in range(0, len(string), width):
        new_str += string[i:i+width] + "\n"
    return new_str

if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)




    