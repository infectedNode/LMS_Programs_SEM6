class Employee:

    count = 0

    def __init__(self, name, code):
        self.name=name
        self.code=code
        Employee.count += 1

    def give_record(self):
        print(Employee.count, end=' ')    
        print(self.name, end=' ')    
        print(self.code)    

name = input()
code = int(input())

obj = Employee(name, code)

obj.give_record()
