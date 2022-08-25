x_and_y = [(x,y)for x in range (1,5) for y in range (1,5)]
XandY = [(x,y) if x > y else (y,x) for x in range (1,5) for y in range (1,5)]
print (x_and_y)
print(XandY)




x_and_y = []
for x in range(1,5):
    for y in range(1,5):
        x_and_y.append((x,y))

print(x_and_y)

listcomp =[num % 3 for num in range(1, 10)]
setcomp = {num % 3 for num in range(1, 10)}
dictcomp = {k:v for k, v in enumerate(range(11, 16),5)}
dictcomp1 = {p:u for p, u in enumerate("Banke",11)}
genexp = (num for num in range(1, 6))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(dictcomp1), dictcomp1)
print(type(genexp), genexp)