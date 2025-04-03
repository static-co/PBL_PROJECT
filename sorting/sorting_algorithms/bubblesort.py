import time

def sort(arr, sorted_arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True

        if not swapped:  # If no swaps, array is already sorted
            break

        if time.time() - start_time > 20:
            print("Took more than 20 seconds")
            return False

    return True
