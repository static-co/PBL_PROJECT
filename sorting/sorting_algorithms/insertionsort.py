import time

def sort(arr, sorted_arr):
    start_time = time.time()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements
            j -= 1
        arr[j + 1] = key  # Place key in the correct position

        if time.time() - start_time > 20:
            print("Insertion Sort took more than 20 seconds.")
            return False

    return True
