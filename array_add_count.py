
a = [1,5,4,2,1,5]
k = int(input("-->"))
count = 0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i] + a[j]) == k:
            count+=1
        else:
            continue
print(count)
