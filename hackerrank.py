def merge_the_tools(string, k):
    # your code goes here
    strings = []
    for i in range(0,int(len(string)/k)):
        strings.append(string[(i*k): (i*k)+k])           
    # print(strings)

    arr = []

    for x in strings:
        for i in x:
            if(i not in arr):
                print(i,end="")
                arr.append(i)
        arr=[]        
        print('\n')

string, k = input(), int(input())
merge_the_tools(string, k)