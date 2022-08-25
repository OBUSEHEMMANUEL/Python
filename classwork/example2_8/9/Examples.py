s = "Hello World"
#help(s.find)
print(s.upper())
print(s.lower())

name = "BANKE OWOLABI"
print(name.title())

print(name.capitalize())

print(name.swapcase())

print(name.startswith('b'))
print(name.startswith('B'))
print(name.startswith('BANKE'))
print(name.endswith('b'))

print(name.ljust(20))
print(name.rjust(20))
print(name.center(20))
print(name.center(20,'@'))

print()
print(name.count('B'))
print(name.find('owo'))
print(name.find('OWO'))

print(name.find('B', 2))
print(name.find('B', 2, 10))
print(name.rindex('B'))

print(name.replace('OWOLABI', "CELINA"))
print(name.replace('B', '@', 1))
print()
name = "    Banke Owolabi\n\t"
print(name)
print(name.strip())

'Banke Owolabi'

b,o = name.split()
print(b)
print(o)

binary = "1011001001"
print(binary.replace("1", "#").replace("0", "1").replace("#","0"))

print(binary.translate(str.maketrans("01", "10")))

name = 'banke owolabi'
print(name.translate(str.maketrans('B', 'b', 'oaw')))
