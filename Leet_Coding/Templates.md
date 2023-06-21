# Code templates

## Two pointers: one input, opposite ends

```
def fn(arr):
    left = ans = 0
    right = len(arr) - 1
    while left < right:
        # Do something with ans
        if COND:
            left += 1
        else:
            right += 1
```

## Two pointers: two inputs exhaust both
```
def fn(arr1, arr2):
    i = j = ans = 0
    while i < len(arr) and j < len(arr2):
         # Do something with ans
        if CONDITION:
            left += 1
        else:
            right += 1
    
    while i < len(arr1):
        # Update ans
        i += 1
    
    while j < len(arr2):
        # Update ans
        j += 1
    
    return ans
```

## Sliding window
def fn(arr):
    left = ans = curr = 0
    for right in range(len(arr)):
        # do logic here to add arr[right] to window
        while WINDOW_COND_BROKEN:
            # Remove element from window
            left += 1
        # Update ans
    return ans
```