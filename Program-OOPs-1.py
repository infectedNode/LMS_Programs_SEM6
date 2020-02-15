class circle:
    #static variable
    pi = 3.14159

    def __init__(self, radius):
        # instance variable
        self.radius = radius

    def area(self):
        return (circle.pi * self.radius * self.radius)

    def circumference(self):
        return (2 * circle.pi * self.radius)

# radius = float(input())

radius = 7.5  # from the question

obj = circle(radius)

print("area=",obj.area())
print("circumference=",obj.circumference())