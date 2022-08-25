
for i in range(1, 11):
    print('*' * i)
print(" ")
print("", end='')

for i in range(1, 11):
    print(('*' * i).rjust(10))
print(' ')
print("", end='')

for i in range(1, 21, 2):
    print(('*' * i).center(20))
print()
print("", end='')

for i in range(1, 11):
    sym = "* " * i
   # print('{:10}'.format(sym))
    print(f'{sym:10}')