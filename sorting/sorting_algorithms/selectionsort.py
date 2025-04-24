import time

def sort(arr, sorted_arr):
    start_time = time.time()

    n = len(arr)
    
    for i in range(n - 1):
        min_index = i  # Assume the first element is the minimum

        for j in range(i + 1, n):  # Find the smallest element in the unsorted part
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap with the first unsorted element
        
        # Check if sorting exceeds 20 seconds
        if time.time() - start_time > 20:
            print("Selection Sort took more than 20 seconds.")
            return False

    return True
