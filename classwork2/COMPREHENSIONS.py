def count(count):
    cont = [num ** 2 for num in range(1, 11)]

    print(count(cont))


coun = [n for n in range(1, 11)]

square = [n ** 2 for n in range(1, 11)]
print(coun)
print(square)

names = ['bimpe', 'Banke', 'abimbola', 'James', 'Olalekan', 'Racheal']
my_names = [name for name in names if name.istitle()]
# my_names=[]
# for name in names:
#   if name.istitle():
#       my_names.append(name)


print(my_names)


number_of_times = int(input("HOW MANY NAMES WILL YOU ENTER"))
input_names = [input(f"{i+1}. Name?") for i in range (number_of_times)]


print(input_names)