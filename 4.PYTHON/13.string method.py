name = '!!!s!!!1HaRry !!!!!!! harry!!!!!'
heading = 'this is nowel'
str = 'Welcome to the console'

print(name.strip('!!'))
print(len(name))
print(name.upper() , name.lower())
print(name.rstrip('!'))
print(name.replace('Ha','Je'))
print(name.split(' '))
print(name.capitalize())
print(name.center(50))
print(heading.title() ,heading.istitle())
print(name.count('r'))
print(str.startswith('to',8,11))
print(str.endswith('to',4,10))
print(str.find("ha"))
print(str.index("co"))
print(str.isalnum())
print(str.isalpha())
print(str.isspace())
print(str.isprintable())
print(str.isupper())
print(str.islower())
print(str.swapcase())

print('-'.join(heading))