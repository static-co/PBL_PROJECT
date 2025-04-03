import random
import time
# Importing sorting algorithms
import sorting_algorithms.bubblesort as bubblesort
import sorting_algorithms.selectionsort as selectionsort
import sorting_algorithms.insertionsort as insertionsort
import sorting_algorithms.mergesort as mergesort
import sorting_algorithms.quicksort as quicksort
import sorting_algorithms.heapsort as heapsort
import sorting_algorithms.radixsort as radixsort
import sorting_algorithms.bucketsort as bucketsort
import sorting_algorithms.timsort as timsort
import sorting_algorithms.bogosort as bogosort

# Dictionary of sorting algorithms
sorting_list_dict = {
    "bubblesort": bubblesort,
    "selectionsort": selectionsort,
    "insertionsort": insertionsort,
    "mergesort": mergesort,
    "quicksort": quicksort,
    "heapsort": heapsort,
    "radixsort": radixsort,
    "bucketsort": bucketsort,
    "timsort": timsort,
    "bogosort": bogosort
}

MAX_ELEMENTS = 10_000_000  # Limit max elements

print("Available Sorting Algorithms:")
for algo in sorting_list_dict:
    print(f"- {algo.capitalize()}")

selected_algo = input("\nEnter sorting algorithm name: ").replace(" ", "").lower()

if selected_algo not in sorting_list_dict:
    print("Invalid selection")
else:
    module = sorting_list_dict[selected_algo]  # Get the selected sorting algorithm

    print(f"\nYou selected: {selected_algo.capitalize()}")

    while True:
        try:
            search_space_size = int(input(f"Enter the number of elements for the search space (max {MAX_ELEMENTS}): "))
            if search_space_size <= 0:
                print("Size must be a positive integer.")
                continue
            if search_space_size > MAX_ELEMENTS:
                print(f"Size must not exceed {MAX_ELEMENTS}. Please enter a lower value.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    data_structure = [random.randint(1, 100) for _ in range(search_space_size)]  # Generate random list
    sorted_arr = sorted(data_structure)  # Reference sorted array

    print(f"\nGenerated Search Space of {search_space_size} elements.")

    start_time = time.time()
    sorted_bool = module.sort(data_structure, sorted_arr)  # Call sorting function
    end_time = time.time()

    if sorted_bool:
        print(f"\n{selected_algo.capitalize()} took {end_time - start_time:.15f} seconds to sort.")
    else:
        print("Couldn't sort")


#radix sort, selection sort, heap sort left