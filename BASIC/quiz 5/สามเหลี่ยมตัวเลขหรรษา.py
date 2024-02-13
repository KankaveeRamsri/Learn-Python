def check_range(n):
    if n < 0 or n >= 10 :
        return "Out of Range"
    return n 


if __name__ == "__main__":
    line = check_range(int(input("Line: ")))
    for i in range(1,line + 1):
        answer = "1" + "".join(str(k) for k in range(2,i+1)) + "".join(str(k) for k in range(i-1, 0, -1))
        print(answer)

if __name__ == "__main__":
    line = check_range(int(input("Line: ")))
    answer = ""
    for i in range(1,line + 1):
        answer += "1" 
    for i in range(1,line + 1):
        answer += "".join(str(k) for k in range(2,i+1)) 
    for i in range(1,line + 1):
        answer += "".join(str(k) for k in range(i-1,0,-1))
        
    print(answer)

