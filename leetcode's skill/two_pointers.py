from typing import List


# Method 1: Naive Approach
# Time Complexity: O(n^2)
def isPairSum1(A, N, X):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if A[i] + A[j] == X:
                return True

            if A[i] + A[j] > X:
                break

    # No pair found with given sum
    return 0


# Method 2: Two Pointers Technique
def isPairSum2(A: List[int], N: int, X: int) -> bool:
    i = 0
    j = N - 1

    while i < j:
        if A[i] + A[j] == X:
            return True

        elif A[i] + A[j] < X:
            i += 1

        else:
            j -= 1

    return False


if __name__ == "__main__":
    arr = [2, 3, 5, 8, 9, 10, 11]
    val = 17
    arrSize = len(arr)
    arr.sort()

    print(isPairSum2(arr, arrSize, val))
