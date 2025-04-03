import random

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

sorting_list_dict = {
    "bubblesort": ("list", bubblesort),
    "selectionsort": ("list", selectionsort),
    "insertionsort": ("list", insertionsort),
    "mergesort": ("list", mergesort),
    "quicksort": ("list", quicksort),
    "heapsort": ("list", heapsort),
    "radixsort": ("list", radixsort),
    "bucketsort": ("dict", bucketsort),
    "timsort": ("list", timsort),
    "bogosort": ("list", bogosort)
}

print("Available Sorting Algorithms:")
for algo in sorting_list_dict:
    print(f"- {algo.capitalize()}")

selected_algo = input("\nEnter sorting algorithm name: ").replace(" ", "").lower()

if selected_algo not in sorting_list_dict:
    print("Invalid selection")
else:
    data_type, module = sorting_list_dict[selected_algo]

    data_structure = [] if data_type == "list" else {}

    print(f"\nYou selected: {selected_algo.capitalize()}")
    print(f"Initialized data structure: {type(data_structure).__name__}")

    while True:
        try:
            search_space_size = int(input("Enter the number of elements for the search space: "))
            if search_space_size <= 0:
                print("Size must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if isinstance(data_structure, list):
        data_structure = [random.randint(1, 100) for _ in range(search_space_size)]
    else:
        data_structure = {i: random.randint(1, 100) for i in range(search_space_size)}

    print(f"\nGenerated Search Space of {search_space_size} elements.")

    # Call the sorting function
    module.sort(data_structure)
