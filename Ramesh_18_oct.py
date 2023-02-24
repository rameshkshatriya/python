
a = int(input("enter a number: "))
b = int(input("enter a number: "))
for i in range(a,b+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")




n = [17,19,18,18,21]
a = set(n)
b = [[],[]]
c = min(n)
while True:
    if n.count(c)>1:
        b[0].append(c)
    if c not in a:
        a.add(c)
        b[1].append(c)
    if len(n)==len(a) and b[0] and b[1]:
        break
    c+=1
print(b)

