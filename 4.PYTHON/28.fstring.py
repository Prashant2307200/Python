letter = 'Hey, my name is {1} and i\'m from {0}'
country = 'India'
name = 'Prashant'

# print(letter.format(name,country))

print(letter.format(country,name))

print(f"Hey my name is {name} and i\'m from {country} country")

txt = "For only price {price:.2f} dollars!"

print(txt.format(price=49.99999))

price = 49.99999

print(f"For only price {price:.2f} dollars!")

print(type(f"{2*30}"))

