a = [1,0,-1,-1,1]
for i in a:
    if a[i]>a[i+1]:
        temp = a[i+1]
        a[i+1] = a[i]
        a[i] = temp
    else:
        
        print(a)
