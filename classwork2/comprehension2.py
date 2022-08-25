evens = [even for even in range(1,11) if even %2 ==0 ]

print(evens)

even_squared_odd_cubbed = [num** 2 if num % 2 ==0 else num ** 3 for num in range(1,11) ]
print(even_squared_odd_cubbed)

