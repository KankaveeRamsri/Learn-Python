def check_bracket(brackets):
    mapping = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    stack = []
    for bracket in brackets:
        if bracket in mapping:
            stack.append(bracket)
        elif bracket in mapping.values():
            # ถ้า stack ว่างหรือวงเล็บปิดไม่ตรงกับวงเล็บเปิดที่อยู่บน stack
            if not stack or mapping[stack.pop()] != bracket:
                return False
    
    return True # ส่งค่า True ออกไปเพราะวงเล็บสมดุลกัน

if __name__ == '__main__':
    brackets = input("Bracket: ")
    if check_bracket(brackets):
        print("Equivalent")
    else:
        print("Not Equivalent")

print("--------------------------------")

def check_bracket(brackets):
    checker = []
    opened_bracket = "{[("
    closed_bracket = "}])"
    for bracket in brackets:
        if bracket in opened_bracket :
            checker.append(bracket)
        elif bracket in closed_bracket :
            if not checker :
                return False
            
            bracket_in_checker = checker.pop()
            index = closed_bracket.index(bracket)
            if opened_bracket[index] != bracket_in_checker :
                return False 
    
    if checker:
        return False 
    
    return True 

if __name__ == '__main__' :
    brackets = input("Bracket: ")
    if check_bracket(brackets):
        print("Equivalent")
    else :
        print("Not Equivalent") 




    