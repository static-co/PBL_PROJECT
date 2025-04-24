import time

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  
    count = [0] * 10  

    # Count occurrences of digits at current place value (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to store actual position of digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the sorted numbers back to original array
    for i in range(n):
        arr[i] = output[i]

def sort(arr, sorted_arr):
    start_time = time.time()

    if len(arr) == 0:
        return True  # Empty array is already sorted

    max_element = max(arr)  
    exp = 1  

    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

        # Check if sorting exceeds 20 seconds
        if time.time() - start_time > 20:
            print("Radix Sort took more than 20 seconds.")
            return False

    return True
