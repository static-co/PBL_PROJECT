import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def sort(arr, sorted_arr):
    start_time = time.time()
    
    arr[:] = quick_sort(arr)  # Sort in place
    
    end_time = time.time()
    
    if end_time - start_time > 20:
        print("Quick Sort took more than 20 seconds.")
        return False

    return True
