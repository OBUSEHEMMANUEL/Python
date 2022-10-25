class Human:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def full_name(self):
        return f"{self.last_name}{self.first_name}"

    def __str__(self):
        return f"Last Name = {self.last_name},First Name = {self.first_name}, Age = {self.age}, sex = {self.sex}"


class Manager(Human):
    def full_name(self):
        return f"{self.last_name[0].upper()}. {self.first_name}"


class Employee(Human):
    def pay_salary(self, salary):
        return salary


employee1 = Employee("Hadiza ", "Umar ", 21, " female")

Employee: employee1 = Employee("Hadiza ", "Umar ", 21, " female")
Manager1: Manager = Manager("Egusi", "Cappy", 65, "Unknown")
# print(employee1)
# print(employee1.full_name())
# print(Manager1.full_name())

human_list = [employee1, Manager1, Human("sapien", "Homo ", 0, "unknown")]

for human in human_list:
    print(human.full_name())
