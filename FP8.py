# Copyright (c) 2020 Shivam Sharma
#
# Licensed under the MIT License (the "License"); 
# you may not use this program except in compliance with the License.
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the program.
#

#Input Strings
string1 = input()
string2 = input()

if(len(string1) != len(string2)):
    # if length is not equal they cannot be anagrams
    print('False')
else:
    # initialising empty Dictionaries
    rec1 = {}
    rec2 = {}

    # storing the count(VALUE) of each alphabet(KEY) in the string
    for i in string1:
        if i in rec1:
            rec1[i] += 1
        else:
            rec1[i] = 1

    for i in string2:
        if i in rec2:
            rec2[i] += 1
        else:
            rec2[i] = 1

    # assuming they are anagrams
    isPossible = 1

    for x in rec1:
        # checking if an alphabet is present in both the records
        if x in rec2:
            # checking the count of an alphabet in records are same
            if(rec1[x] != rec2[x]):
                isPossible = 0
                break
        else:
            isPossible = 0
            break

    # Printing Result
    if(isPossible == 1):
        print('True')
    else:
        print('False')