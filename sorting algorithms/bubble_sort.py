import time
import random
def bubbleSort(arr):
    swapped = False
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True 
        
        if swapped: 
            swapped = False 
        else:
            break 
    
    return arr 

if __name__ == '__main__':
    arr = [random.randint(1,1000) for _ in range(10000)]
    start_time = time.time()
    bubbleSort(arr)
    end_time = time.time()
    print((" Bubble Sort ").center(30,'-'))
    print(f"Time taken to sort an array of size {10000}: {round(end_time - start_time,2)} seconds")