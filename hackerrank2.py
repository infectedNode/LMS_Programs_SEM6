value = input().split(" ");
# print(input)

squareSum = 0

for i in range(0,int(value[0])):
    # values.append(input().split(" "))
    one = input().split(" ")
    for x in one:
        one[x]
    one.sort()
    print(one)
    maxnum = int(one[-1])
    print(maxnum)
    squareSum += (maxnum * maxnum)

print(int(value[1])%squareSum)