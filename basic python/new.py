def sequential_search(arr, target):
 for index, element in enumerate(arr):
   if element == target:
    return index # Element found, return its index
 return -1 # Element not found
# Example usage:
my_list = [10, 20, 30, 40, 50, 60, 70]
target_element = 40
result = sequential_search(my_list, target_element)
if result != -1:
 print(f"Element {target_element} found at index {result}.")
else:
 print(f"Element {target_element} not found in the list.")
