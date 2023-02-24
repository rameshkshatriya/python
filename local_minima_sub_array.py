import time

def local_minima_sub_array(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    # Binary search
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        elif arr[mid] > arr[mid - 1]:
            left = mid + 1
        else:
            return arr[mid]
    return arr[left]

l=[2,2,1,-3,4,3,1,-8,6,-2,-1]
s=time.time()
print(local_minima_sub_array(l))
e =time.time()
print("running time: ", e-s )


output = 2
running time:  0.0003299713134765625