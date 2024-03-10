dic = {
    "Harry" : 39,
    "Raj" : 59,
    "Ram": 90
}

print(dic["Ram"])

# del dic
# del dic["Raj"]

print(dic.get("Raj"))

for key in dic.keys():
    print(key)

for val in dic.values():
    print(val)

for key ,val in dic.items():
    print(key, val)