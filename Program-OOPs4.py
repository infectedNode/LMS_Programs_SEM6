class Count:
    def __init__(self, string):
        self.string = string
        self.upper = 0
        self.vowels = 0

    def counter(self):
        for i in self.string:
            if(i.isupper()):
                self.upper += 1
            if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                self.vowels += 1

obj = Count(input())

obj.counter()

print(obj.upper, obj.vowels)