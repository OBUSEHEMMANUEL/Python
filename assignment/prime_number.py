def prime_number():
    num = int(input("Enter number: "))

    flag = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
             flag = True
            break
    if flag:
        print(num, "is a not prime number")
    else:
        print(num, "is  a prime number")
prime_number()




