def process_number(number):
    shift_amount = 2 if number % 2 == 0 else 3
    return (number ^ (number << shift_amount)) % 13

def main():
    stack = []  # สร้างสแต็กเปล่า

    while True:
        number = int(input("Enter number: "))  # รับตัวเลขจากผู้ใช้
        operation_index = process_number(number)  # ประมวลผลตัวเลข

        # ตารางการสุ่มตัวดำเนินการ
        operations_even = ["push", "pop", "pop", "head", "push", "close", "head", "push", "pop", "push", "pop", "close", "head"]
        operations_odd = ["push", "close", "pop", "head", "pop", "pop", "push", "push", "pop", "push", "push", "head", "close"]

        # เลือกตัวดำเนินการตาม number
        action = operations_even[operation_index] if number % 2 == 0 else operations_odd[operation_index]

        # ดำเนินการตามตัวดำเนินการ
        if action == "push":
            stack.append(number)
            print(f"Push: {number}")
        elif action == "pop" and stack:
            popped = stack.pop()
            print(f"Pop: {popped}")
        elif action == "head" and stack:
            print(f"Head: {stack[-1]}")
        elif action == "close":
            print("Close")
            break

        print(f"Stack: {stack}")
    
    print("End of program, Bye!")

if __name__ == "__main__":
    main()
