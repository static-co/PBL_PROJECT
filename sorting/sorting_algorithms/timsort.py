import time

def sort(arr, sorted_arr):
    start_time = time.time()

    arr[:] = sorted(arr)  
    
    end_time = time.time()
    
    if end_time - start_time > 20:
        print("Timsort took more than 20 seconds.")
        return False

    return True 
