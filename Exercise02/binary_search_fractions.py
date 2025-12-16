from typing import List, Tuple, Union

def binary_search_upper_bound(array: List[float], target: float) -> Tuple[int, Union[float, None]]:
    low = 0
    high = len(array) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if array[mid] == target:
            upper_bound = array[mid]
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else: # array[mid] > target
            upper_bound = array[mid]
            high = mid - 1
    return (iterations, upper_bound)



# Example usage:
fractions = [0.1, 0.25, 0.33, 0.5, 0.66, 0.75, 0.9]
target = 0.5
result = binary_search_upper_bound(fractions, target)
print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")