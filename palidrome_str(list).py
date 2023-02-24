


answer = lambda x,y :[i for i in range(x,y) if i == int(str(i)[::-1])]
print(answer(10,1000))

a = ["1 2 3 4 5 6"]
print([int(i) for i in a[0].split()])