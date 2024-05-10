import time 
import random

MIN_MERGE = 32

def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = arr[l:m+1], arr[m+1:r+1]
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def tim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n)
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + size * 2 - 1), (n-1))
            merge(arr, left, mid, right)
        size *= 2

if __name__ == "__main__":
    size = 1000000
    arr = [random.randint(1,1000) for _ in range(size)]
    start_time = time.time()
    tim_sort(arr)
    end_time = time.time()
    print((" Tim Sort ").center(30,'-'))
    print("Time taken to sort an array of size {} : {:.2f} seconds".format(size,end_time - start_time))