x = 4

def hello():
    global x
    x = 5
    # x = 5
    print(x)
    print("Hi, Good morning!")

hello()

print(x)