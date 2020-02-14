class test:
    def __init__(self,one,two):
        self.one = one
        self.two = two

    def display(self):
        print('Testing Method 1 ' + str(self.one))
        print('Testing Method 2 ' + str(self.two))

    def add(self):
        sum = self.one + self.two
        print('Addition of two arguments is ' + str(sum))

one = int(input())        
two = int(input())

obj = test(one, two)

obj.display()

obj.add()