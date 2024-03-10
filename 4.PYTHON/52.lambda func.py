def apply(fx,value):
    return fx(value)

half = lambda x : x/2
print(half(10))

avg = lambda x,y : (x+y)/2
print(avg(10,20))

sum = lambda x,y,z : x+y+z
print(sum(10,20,30))

print(apply(half,20)) 
print(apply(lambda x : x/2,20)) 