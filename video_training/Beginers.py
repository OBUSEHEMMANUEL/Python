def Example16():
    course = 'Python For Beginners'
    print(len(course))
    print(course.find('n'))
    print(course.replace('Beginners', "Absolute Beginner"))
    print(course.title())
Example16()

def Example17():
    f_name ="john"
    l_name = "smith"
    message = f'{f_name} [{l_name}] is a coder '
    print(message)

def Example18():
    weight =(int(input("what is your weight in pound: ")))
    kilogram = weight * 0.454
    print(kilogram)

def Example19():
    name ='john smith'
    age = 28
    name = input("what is your name? ")
    color = input("what is your favourite colour? ")
    print(name + " likes "+ color )

def Example20():
    birth_year = (int(input ("Enter birth year?")))
    age = 2022 - birth_year
    print(age)