s = input()

def display(a, b):

count = 0

for i in s:
    if(i == 0):
        count += 1
    elif(s[i] == s[i-1]):
        count += 1
    elif(s[i] != s[i-1]):
        count
        display(count, i)

