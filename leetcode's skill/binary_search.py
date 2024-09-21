# def binary_search(arr, low, high, x):
#     mid = (high + low) // 2

#     if arr[mid] == x:
#         return mid

#     elif arr[mid] < x:
#         return binary_search(arr, mid + 1, high, x)

#     else:  # arr[mid] > x
#         return binary_search(arr, mid - 1, high, x)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr = [1, 22, 33, 4, 5, 6, 7, 8, 9, 10]

    x = 9
    val = binary_search(arr, 0, len(arr), x)
    print(val)
