class Students:

    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def average(self):
        sum = 0
        for x in self.marks:
            sum += x
        return (sum/len(self.marks))

# name = input()

name = "Shivam"

obj = Students(name)

mark1 = float(input())            
mark2 = float(input())

obj.add_marks(mark1)
obj.add_marks(mark2)

print(obj.average())