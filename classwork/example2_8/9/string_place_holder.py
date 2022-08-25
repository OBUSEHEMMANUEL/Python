print("sorry, is this the {} minute {}?".format(5, 'ARGUMENT'))

s = "{:^10} is {} years old".format("Bill", 25)
print(s)

print(list(enumerate("mississippi")))

river = 'mississippi'
target = input('Input a character to find: ')
for index, letter in enumerate(river):
    if letter == target:
        print("letter found at index: ", index)
        break
    else:
        print('letter',target,'not found in', river)

print()

print('{0} is {2} and {0} is also {1}'. format('Bill', 25, 'tall'))