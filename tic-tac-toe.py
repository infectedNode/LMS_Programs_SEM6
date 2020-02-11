# Copyright (c) 2020 Shivam Sharma
#
# Licensed under the MIT License (the "License"); 
# you may not use this program except in compliance with the License.
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the program.
#

# Display the board with current position marked
def displayBoard(status):
    print("   {}\t|  {}\t|  {}".format(status[0],status[1],status[2]).expandtabs(6))
    print(" ----- ----- -----")
    print("   {}\t|  {}\t|  {}".format(status[3],status[4],status[5]).expandtabs(6))
    print(" ----- ----- -----")
    print("   {}\t|  {}\t|  {}".format(status[6],status[7],status[8]).expandtabs(6))

# Check for a Win
def check(status,marker):
    if(marker == 'X'):
        if(status[0] == 'X' and status[1] == 'X' and status[2] == 'X'):
            return True
        elif(status[3] == 'X' and status[4] == 'X' and status[5] == 'X'):
            return True
        elif(status[6] == 'X' and status[7] == 'X' and status[8] == 'X'):
            return True        
        elif(status[0] == 'X' and status[3] == 'X' and status[6] == 'X'):
            return True    
        elif(status[1] == 'X' and status[4] == 'X' and status[7] == 'X'):
            return True    
        elif(status[2] == 'X' and status[5] == 'X' and status[8] == 'X'):
            return True    
        elif(status[0] == 'X' and status[4] == 'X' and status[8] == 'X'):
            return True    
        elif(status[2] == 'X' and status[4] == 'X' and status[6] == 'X'):
            return True    
        else:
            return False
    elif(marker == 'O'):
        if(status[0] == 'O' and status[1] == 'O' and status[2] == 'O'):
            return True
        elif(status[3] == 'O' and status[4] == 'O' and status[5] == 'O'):
            return True
        elif(status[6] == 'O' and status[7] == 'O' and status[8] == 'O'):
            return True        
        elif(status[0] == 'O' and status[3] == 'O' and status[6] == 'O'):
            return True    
        elif(status[1] == 'O' and status[4] == 'O' and status[7] == 'O'):
            return True    
        elif(status[2] == 'O' and status[5] == 'O' and status[8] == 'O'):
            return True    
        elif(status[0] == 'O' and status[4] == 'O' and status[8] == 'O'):
            return True    
        elif(status[2] == 'O' and status[4] == 'O' and status[6] == 'O'):
            return True    
        else:
            return False
    else: 
        return False        



mark1 = input('Player 1, what marker will you choose ( X or O ): ').upper()

if(mark1 == 'X'):
    mark2 = 'O'
else:
    mark2 = 'X'

# Initialising board with nothing marked
boardStatus = ['','','','','','','','',''];

# Player 1 play first
turn = 1

while(True):
    print('\n\n')
    displayBoard(boardStatus)
    if(turn == 1):
        pos = int(input('\n\nPlayer 1 ( {} ), Enter next position (1-9): '.format(mark1)))
        
        # If that postion is already marked
        if(boardStatus[pos-1] != ''):
            print('\n\nThis Position is already marked !')
            continue

        boardStatus[pos-1] = mark1
        res = check(boardStatus, mark1)
        if(res == True):
            print('\n\n')
            displayBoard(boardStatus)
            print('\n\n*** Congratulations Player 1 ( {} ), You Win! ***'.format(mark1))
            break
        turn = 2
    elif(turn == 2):
        pos = int(input('\n\nPlayer 2 ( {} ), Enter next position (1-9): '.format(mark2)))
        
        # If that postion is already marked
        if(boardStatus[pos-1] != ''):
            print('\n\nThis Position is already marked !')
            continue
        
        boardStatus[pos-1] = mark2
        res = check(boardStatus, mark2)
        if(res == True):
            print('\n\n')
            displayBoard(boardStatus)
            print('\n\n*** Congratulations Player 2 ( {} ), You Win! ***'.format(mark2))
            break
        turn = 1

    # Condition for a draw
    isDraw = 1
    for x in boardStatus:
            if(x == ''):
                isDraw = 0
                break 

    if(isDraw == 1):
        print('\n\n')
        displayBoard(boardStatus)
        print('\n\n*** Game Draw! ***')
        break