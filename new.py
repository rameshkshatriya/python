def func():
    text = "joyful"
    name = (lambda x :text+" "+x)
    return name

msg = func()
print(msg("life"))