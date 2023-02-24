import time

def sub_array(n):
    count = 0
    for x in range(len(n)):
        for y in range(x+1, len(n)+1):
            subarray = n[x:y]
            if sum(subarray) == 0:
                count = max(count, len(subarray))
    return count


l = [2, 2, 1, -3, 4, 3, 1, -8, 6, -2, -1]
s=time.time()
print(sub_array(l))
e =time.time()
print("running time: ", e-s )


output = 8
running time:  0.0005102157592773438


