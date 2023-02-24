a = "{}"
b = []
for i in a:
    if i in "({[":
        b.insert(0,i)
    else:
        if b:
            if b[0]+i in ['()','{}','[]']:
                b.pop(0)
            else:
                print("false")
        else: 
            print("false")

if not b:
    print("true")
else:
    print("false")