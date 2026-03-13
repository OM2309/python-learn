# class Basic:

#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

#     def info(self):
#         print("Name:", self.name)
#         print("Role:", self.role)


# user1 = Basic("Anurag", "Developer")

# user1.info()


class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print(calc.add(5, 3))
print(calc.multiply(4, 2))