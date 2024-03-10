names = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(type(names))

for idx in range(5):
    print(names[idx])

length = len(names)

print(length)
print(names[0 : length : 1])
print(names[:])
print(names[::])
print(names[::-1])
print(names[::length-1])
print(names[::])
print(names[:5])
print(names[:-10])
print(names[:length-10])
print(names[7:])
print(names[-8: ])
print(names[length-8: ])

if 7 in names:
    print('yes')

if 'ha' in 'harry':
    print('yes')

marks = [i*i for i in range(15) if i%2 == 0]
print(marks)