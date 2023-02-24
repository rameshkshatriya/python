
import time
def sub_array(n):
    hash_map= {}
    a=0
    b=0
    for i in range(len(n)):
        b += n[i]
        if b ==0:
            a=i+1
        if b in hash_map:
            a = max(a, i-hash_map[b])
        else:
            hash_map[b]=i
    return a

l=[2,2,1,-3,4,3,1,-8,6,-2,-1]
s=time.time()
print(sub_array(l))
e =time.time()
print("running time: ", e-s )


output = 8
running time:  0.0006899833679199219