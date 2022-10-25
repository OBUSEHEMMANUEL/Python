a_list = []
for number in range(1, 6):
    a_list.append(number)
print(a_list)

letters = []
letters += 'python'
print(letters)

list1 = [10, 20, 30]
list2 = [40, 50, 'red']
concatenated_list = list1 + list2
print(concatenated_list)

for i in range(len(concatenated_list)):
    print(f"{i} = {concatenated_list[i]}")

list3_ = [5, 7, (4, 5), 9, 0]
print(list3_)

single = ('red',)
print(single)

number1 = 99
number2 = 22
number1, number2 = [number2, number1]
print(f"number1 = {number1}, number2 = {number2}")

colours = ['red', 'blue', 'green']
print(list(enumerate(colours)))
print(tuple(enumerate(colours)))

list1 = [10, 20, 30]
list1 += (24, 7)
print(list1)


def f(my_list=[]):
    my_list.append('###')
    return my_list


print(f())

print(f(['foo', 'bar', 'baz']))


def f(my_list=None):
    if my_list is None:
        my_list = []
        my_list.append('###')
        return my_list


print(f())
print(f())


def f(x):
    x[0] = '___'


my_list = ['foo', 'bar', 'baz', 'qux']

f(my_list)
print(my_list)


student_tuple = [4, 7, [8, 6], 3, 4]
student_tuple[2][1] = 3
student_tuple[3] =9
print(student_tuple)

colors = ['red', 'orange', 'yellow']
print(list(enumerate(colors)))

for index, value in enumerate(colors):
    print(f"{index}: {value}")