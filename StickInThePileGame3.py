#660631097 Tanasin Sriwichai
#HW1D_stickpile
#12-7-2023

import random

def take_stick (n_take,n_sticks):#define function for take stick from the pile game.
    if n_take > 2: #1st condition check the limit number of taken stick and amount of stick left.
        print('No you cannot take more than 2 sticks!\n')
    elif n_take < 1:
        print('No you cannot take less than 1 stick!\n')
    elif n_take > n_sticks:
        print('There are no enough sticks to take.\n')
    else :
        n_sticks -= n_take #take the stick from the pile.
        if n_sticks == 1:#2nd condition check how many stick left after taken out.
            print('There are',n_sticks,'stick in the pile.\n')
        elif n_sticks > 0: 
            print('There are',n_sticks,'sticks in the pile.\n')
    return n_sticks


n_stick = int(input('How many sticks (N) in the pile:'))
print('There are {} sticks in the pile'.format(n_stick))
name = input('What is your name :')

while n_stick > 0: #create while loop until number of stick was out
    remainder = n_stick 
    while n_stick == remainder: #check that the stick was taken out by remainder.
        n_out = int(input('{}, how many sticks you will take (1 or 2):'.format(name)))
        n_stick = take_stick(n_out,n_stick)
        if n_stick == 0: #save the value of indicator for finding winner 0 for user and 1 for computer.
            indicator = 0
    if n_stick >= 1:
        if n_stick > 1:
            remainder = n_stick
            while n_stick == remainder:#check that the stick was taken out by remainder.
                n_bot_out = random.randint(1,2)
                print('I, smart computer, takes :',n_bot_out)
                n_stick = take_stick(n_bot_out,n_stick)
        elif n_stick == 1: #save the value of indicator for finding winner 0 for user and 1 for computer.
            indicator = 1
            break
                
        

if indicator == 0: #Display winner!!
    print(name,', takes the last stick.\n')
    print('I,smart computer, win !!!!')
else:
    print('I, smart computer, takes the last stick.\n')
    print(name,'win, (I, smart computer, am sad T_T)')