


a = int(input("enter a number: "))
b = int(input("enter a number: "))
sum = 0
for i in range(a,b+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            sum = sum + i
print(sum, end=" ")
