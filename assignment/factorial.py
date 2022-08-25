import math

num = int(input("Enter number: "))
def factorial(n):

    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


print("factorial of", num, "is", factorial(num))

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return math.factorial(num)
print("factorial of", num, "is", factorial(num))

print("factorial of", num, end=" ")
for i in range(num-1, 1, -1):
    num*= i
print( "is", num)

