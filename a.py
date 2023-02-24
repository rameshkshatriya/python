st = "I code in python"
n =len(st)
result = [0]*n
for i in range(n):
    if (st[i] == " "):
        result[i] = " "
j = n-1
for i in range(len(st)):
    if (st[i] != " "):
        if (result[j] == " "):
            j-=1
        result[j] = st[i]
        j-=1
print("".join(result))