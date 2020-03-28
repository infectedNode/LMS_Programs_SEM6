class Gates:

    @staticmethod
    def AND(num1, num2):
        if(num1 == '1' and num2 == '1'):
            return 1
        else:
            return 0

    @staticmethod
    def OR(num1, num2):
        if(num1 == 0 and num2 == 0):
            return 0
        else:
            return 1

    @staticmethod
    def NOT(num):
        if(num == 1):
            return 0
        else:
            return 1                    

obj = Gates()            
pins = input().split(' ')

f1 = obj.AND(pins[0], pins[1])
f2 = obj.AND(pins[2], pins[3])

s = obj.OR(f1, f2)

t = obj.NOT(s)

print(t)