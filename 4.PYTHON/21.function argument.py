# a is required and c is default
def average(a, b=4, c=1):
    print("The average is ", (a + b + c) / 2)

# keyword arg
average(1,2)
average(1)
average(1,c=4)

# variable length arg

# arbitory arg
def avg(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum/len(nums)

print(avg(1,2,3,4,5))

# keyword arb. arg.

def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")
