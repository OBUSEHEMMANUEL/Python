number = list(range(1, 16))
even_number = number[1:len(number):2]

number[5:10] = [0] * len(number[5:10])
print(number)
number = number[0:5]
print(number)
del number[6:]
print(number)

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)

letters = 'fadgchjebi'
l = sorted(letters)
print(l)
foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']
foods.sort()
print(foods)

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6, 1000]
key = 1000
if key in numbers:
    print(f'{key} at index {numbers.index(key)}')
else:
    print(f'{key} not found')

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times')
