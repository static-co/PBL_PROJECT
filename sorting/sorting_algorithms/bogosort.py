import random
import time
def is_sorted(arr, sorted_arr):
    return arr == sorted_arr  # Compare with pre-sorted array

def sort(arr, sorted_arr):
    start_time = time.time()
    while not is_sorted(arr, sorted_arr):
        if time.time() - start_time > 20:
            print("took more than 20 seconds")
            return False
        random.shuffle(arr)
    return True
        