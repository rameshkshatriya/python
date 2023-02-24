a = [2,4,1,8,12,3,5,9,0,-2]
# print(sorted(a))
# b = []
# for i in range(len(a)):
#     x = min(a)
#     b.append(x)
#     a.remove(x)
# print(b)       
i = 0
x = len(a)-1
j = x
while True:
    if a[j]<a[i]:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    j-=1
    if j == i:
        j = x
        i+=1
    if i == x:
        break
    print(a)

print(a)


        

        






