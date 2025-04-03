import time

def merge_sort(arr, start_time):
    if time.time() - start_time > 20:  # Stop if more than 20 sec
        return False  

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        if not merge_sort(left_half, start_time):  # Check time in recursion
            return False
        if not merge_sort(right_half, start_time):
            return False

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return True

def sort(arr, sorted_arr):
    start_time = time.time()
    sorted_successfully = merge_sort(arr, start_time)
    
    if not sorted_successfully:
        print("Merge Sort took more than 20 seconds.")
        return False

    return True
