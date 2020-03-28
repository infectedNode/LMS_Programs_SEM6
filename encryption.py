import math

s = input()
word = s.strip(" ").split(" ")
newString = ''
for x in word:
    newString += x    

squareRoot = math.sqrt(len(newString)) 

row = math.floor(squareRoot) 
col = math.ceil(squareRoot)

finalString = ''

for i in range(0,col):
    for j in range(0, row+1):
        try:
            finalString += newString[(col*j)+i]
        except:
            finalString += ''
    finalString += ' '

print(finalString) 
