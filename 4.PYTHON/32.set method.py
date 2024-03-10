marks1 = {1,2,3,4,5}
marks2 = {1,2,4,5,10,11}

print(marks1.union(marks2))

# marks1.update(marks2)
# print(marks1)

print(marks1.intersection(marks2))

# marks1.intersection_update(marks2)
# print(marks1)

print(marks1.symmetric_difference(marks2))

# marks1.symmetric_difference_update(marks2)
# print(marks1)

print(marks1.difference(marks2))

# marks1.difference_update(marks2)
# print(marks1)

print(marks1.isdisjoint(marks2))

marks3 = {1,2,3,4,5,10,11}
marks4 = {1,3,5}

print(marks3.issuperset(marks4))
print(marks4.issubset(marks3))

marks4.remove(3)
marks4.discard(3)
marks4.pop()
marks4.clear()
marks4.add(5)
print(marks4)


del marks3
# print(marks3)
