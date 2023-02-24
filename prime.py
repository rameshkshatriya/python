n = int(input("enter a number: "))
temp = 0
for i in range(1,n+1):
    if n % i == 0:
        temp+=1
if temp>2:
    print("it is not a prime")
else:
    print("it is prime")