# a = [1,2,3,-1,-2,-3]
# b = []
# for i in range(len(a)):
#     c = min(a)
#     b.append(c)
#     a.remove(c)
# print(b)
# for i in range(len(a)):
#     print(i)
#     if a[i] < 0:
#         b.append(i)
#     print(b)
a = [1,2,3,-1,-2,-3]
temp = 0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    print(a)


