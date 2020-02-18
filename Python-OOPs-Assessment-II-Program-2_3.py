class Calculator:
    @staticmethod
    def add(num1, num2):
        print(num1+num2)

    @staticmethod
    def sub(num1, num2):
        print(num1-num2)

    @staticmethod
    def mul(num1, num2):
        print(num1*num2)

    @staticmethod
    def div(num1, num2):
        print(num1/num2) 

print('Select operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')

choice = int(input('Enter choice(1/2/3/4): '))
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

obj = Calculator()                   

if(choice == 1):
    obj.add(num1, num2)
elif(choice == 2):
    obj.sub(num1, num2)
elif(choice == 3):
    obj.mul(num1, num2)   
elif(choice == 4):
    obj.div(num1, num2)         