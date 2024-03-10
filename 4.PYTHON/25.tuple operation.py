countries = ("india","england","canada")
temp = list(countries)
temp.append("Pakistan")
temp[1] = "China"
temp.pop(0)
countries = tuple(temp)
print(countries)