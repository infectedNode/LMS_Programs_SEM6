# Copyright (c) 2020 Shivam Sharma
#
# Licensed under the MIT License (the "License"); 
# you may not use this program except in compliance with the License.
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the program.
#

term = int(input())

def nthFib(n1, n2, term):
    sum = n1 + n2
    if(term <= 0):
        print(sum)
    else:
        term -= 1
        nthFib(n2, sum, term)    

if(term == 0):
    print(0)
elif(term == 1):
    print(1) 
else:
    term -= 2
    nthFib(0,1,term)           

