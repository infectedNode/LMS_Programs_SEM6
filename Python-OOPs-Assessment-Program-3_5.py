class power:
    def calculate(self,num,pow):
        return (num**pow)

obj = power()

num = int(input())         
pow = int(input()) 

print(obj.calculate(num,pow))