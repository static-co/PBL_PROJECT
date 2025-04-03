import time

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def sort(arr, sorted_arr):
    start_time = time.time()
    
    if not arr:
        return True
    
    num_buckets = len(arr) // 10 or 1  # Create buckets based on data size
    buckets = [[] for _ in range(num_buckets)]
    
    max_val = max(arr)
    min_val = min(arr)
    range_val = (max_val - min_val) / num_buckets if max_val != min_val else 1

    # Distribute elements into buckets
    for num in arr:
        if time.time() - start_time > 20:
            print("Took more than 20 seconds")
            return False
        index = int((num - min_val) / range_val)
        index = min(index, num_buckets - 1)  # Avoid out-of-bounds index
        buckets[index].append(num)

    # Sort each bucket and merge
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(insertion_sort(bucket))

    arr[:] = sorted_list  # Update original list
    return True
