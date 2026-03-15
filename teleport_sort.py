import random

def teleport_sort(arr):

    iterations = 0
    while not is_sorted(arr):
        i = random.randint(0, len(arr) - 1) # element to move
        j = random.randint(0, len(arr) - 1) # destination    

        value = arr.pop(i)
        arr.insert(j, value)
        iterations += 1

    return arr, iterations

def is_sorted(arr):
    i = 0
    while i < len(arr) - 1:
        
        if arr[i] > arr[i + 1]:
            return False
        
        i += 1

    return True