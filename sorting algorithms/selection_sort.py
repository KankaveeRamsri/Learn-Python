import random
import time
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for idx in range(i + 1, n):
            if arr[idx] < arr[min_idx]:
                min_idx = idx 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr 

if __name__ == '__main__':
    arr = [random.randint(0,1000) for _ in range(10000)]
    start_time = time.time()
    selectionSort(arr)
    end_time = time.time()
    print((" Selection Sort ").center(30,'-'))
    print(f"Time taken to sort an array of size {10000}: {round(end_time - start_time,2)} seconds")