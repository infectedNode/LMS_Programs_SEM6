import time,os

def display(status):
    print("\t{}\t{}\t\t{}\t{}".format(status[0],status[1],status[2],status[3]).expandtabs(3))
    print("{}\t\t\t{}\t\t\t{}".format(status[4],status[5],status[6]).expandtabs(3))
    print("{}\t\t\t\t\t\t{}".format(status[7],status[8]).expandtabs(3))
    print("\t{}\t\t\t\t{}".format(status[9],status[10]).expandtabs(3))
    print("\t\t{}\t\t{}".format(status[11],status[12]).expandtabs(3))
    print("\t\t\t{}".format(status[13]).expandtabs(3))

for i in range(0,100):
    if(i<15):
        status = ['*','*','*','*','*','*','*','*','*','*','*','*','*','*']
        display(status)
    else:
        if(i%2 == 0):
            status = ['*','','','*','','*','','*','*','','','*','*','']
            display(status)
        else:
            status = ['','*','*','','*','','*','','','*','*','','','*']
            display(status)
    time.sleep(.03)
    os.system('cls')