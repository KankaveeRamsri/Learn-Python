def is_balanced(parentheses):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in parentheses:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

if __name__ == "__main__":
    input_str = input("Enter parentheses: ")
    if is_balanced(input_str):
        print("Balanced parentheses")
    else:
        print("Unbalanced parentheses")





    