# ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่


def is_even(num):
    return (num & 1) == 0


if __name__ == "__main__":
    print(is_even(4))
    print(is_even(7))
