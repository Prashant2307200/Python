
# cube = lambda x: x*x*x

# list = [1,2,3,4,5,6]
# cube_list = []

# for item in list:
#     cube_list.append(cube(item))

# print(cube_list)

# cube_list = list(map(lambda x : x*x*x,[1,2,3,4,5]))
# print(cube_list)



# s = '  The   sky is  blue        '
# print(list(filter(lambda ch : ch != "",s.split(' ')[::-1])))
# new_str = ' '.join(list(filter(lambda ch : ch != "",s.split(' ')[::-1]))).strip(' ')
# s = ' '.join(s.split()[::-1])
# print(s)

reduced_val = reduce(lambda x,y:x+y , [1,2,3,4,5])
print(reduced_val)