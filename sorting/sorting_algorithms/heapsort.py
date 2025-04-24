import time

def heapify(arr, n, i, start_time):
    if time.time() - start_time > 20:
        return False  # Stop if time exceeds 20 sec

    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        if not heapify(arr, n, largest, start_time):  
            return False  

    return True  

def heap_sort(arr, start_time):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        if not heapify(arr, n, i, start_time):  
            return False  

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        if time.time() - start_time > 20:
            return False  

        arr[i], arr[0] = arr[0], arr[i]  
        if not heapify(arr, i, 0, start_time):  
            return False  

    return True  

def sort(arr, sorted_arr):
    start_time = time.time()

    if not heap_sort(arr, start_time):  
        print("Heap Sort took more than 20 seconds.")
        return False  

    return True  
