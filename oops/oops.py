class Basic:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def info(self):
        print("Name:", self.name)
        print("Role:", self.role)


user1 = Basic("Anurag", "Developer")

user1.info()
