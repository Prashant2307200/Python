lst = [1,34,2,3,4,5,6,7,8,9,10,11]

popped = lst.pop()
print(lst ,popped)

popped2 = lst.pop(3)
print(lst ,popped2)

lst.append(12)
print(lst)

lst.sort(reverse=True)
print(lst)

lst.reverse()
print(lst)

print(lst.index(34))

print(lst.count(34))

newLst = lst.copy()
newLst.append(23)
print(newLst)

lst.insert(2,100)
print(lst)

anotherLst = lst + newLst
print(anotherLst)

lst.extend(anotherLst)
print(lst)

