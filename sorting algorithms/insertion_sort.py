import random
import time
def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
    return arr 

if __name__ == "__main__":
    arr = [random.randint(1,1000) for _ in range(10000)]
    start_time = time.time()
    insertionSort(arr)
    end_time = time.time()
    print((" Insertion Sort ").center(30,'-'))
    print(f"Time taken to sort an array of size 10000: {round(end_time - start_time,2)} seconds")