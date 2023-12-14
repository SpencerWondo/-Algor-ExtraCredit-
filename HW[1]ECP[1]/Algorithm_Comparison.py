import random
import time

# Insertion Sort Function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# West Haven Sort Function
def westhavensort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Algorithm Comparison Function
def compare_algorithms():

    random_input = [random.randint(1, 10000) for _ in range(10000)]

    algorithms = {
        "Insertion Sort  ": insertion_sort,
        "Merge Sort      ": merge_sort,
        "West Haven Sort ": westhavensort
    }

    fastest_algo = None
    fastest_time = float('inf')

    for algo_name, algo_func in algorithms.items():

        arr = random_input.copy()
    
        start_time = time.time()
        algo_func(arr)
        end_time = time.time()
    
        time_taken = end_time - start_time

        print(f"\t{algo_name} took:[{end_time - start_time:.6f} secs]")
    
        if time_taken < fastest_time:
            fastest_time = time_taken
            fastest_algo = algo_name.strip()
    
    print(f"\nFastest algorithm: [{fastest_algo}] Taking: [{fastest_time:.6f} secs]")
    
# Run comparison

print("Sorting Algorithm Time Comparison\n")
print("\tRandom number input 10,000 numbers\n")

compare_algorithms()