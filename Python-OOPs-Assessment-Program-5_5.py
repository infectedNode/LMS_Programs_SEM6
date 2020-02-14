class rev:
    def reverse(self, string):
        lst = string.split(' ')
        lst.reverse()

        for x in lst:
            print(x, end=' ')

string = input()

obj = rev()

obj.reverse(string)