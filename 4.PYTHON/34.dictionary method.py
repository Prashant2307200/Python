dic = {
    "Harry" : 39,
    "Raj" : 59,
    "Ram": 90
}

dic2 = {
    "Mahesh" : 32,
    "Djkstra" : 99
}

dic.update(dic2)
# dic.clear()
# del dic
# del dic["Raj"]
# dic.popitem()
dic.pop('Raj')

print(dic)