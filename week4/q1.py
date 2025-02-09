def get_min(arr):    
    min_val = arr[0] 
    
    for num in arr:
        if num < min_val:
            min_val = num 
            
    return min_val

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Minimum element:", get_min(arr))