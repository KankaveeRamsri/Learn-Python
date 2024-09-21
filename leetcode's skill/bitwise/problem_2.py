# นับจำนวน bit ที่เป็น 1


def count_ones(num):
    count = 0
    while num > 0:
        count += num & 1
        num >> 1
    return count


if __name__ == "__main__":
    print(count_ones(7))
    print(count_ones(10))
