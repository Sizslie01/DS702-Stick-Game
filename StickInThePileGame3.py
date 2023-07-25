#660631097 Tanasin Sriwichai
#HW1E_stickpile
#26-7-2023
import random

name = input('What is your name :')
n_sticks = int(input('How many sticks (N) in the pile:'))
print('There are {} sticks in the pile'.format(n_sticks))

def user_take_stick (n_of_sticks, take_not_more_than = 2, winner_condition = 1):
    n_take = int(input('How many you will take (1 or 2):'))
    if n_take > take_not_more_than: #1st condition check the limit number of taken stick and amount of stick left.
        print('No you cannot take more than 2 sticks!\n')
    elif n_take < winner_condition:
        print('No you cannot take less than 1 stick!\n')
    elif n_take > n_of_sticks:
        print('There are no enough sticks to take.\n')
    else:
        n_of_sticks -= n_take
        if n_of_sticks == winner_condition:#2nd condition check how many stick left after taken out.
            print('There are',n_of_sticks,'stick in the pile.\n')
        elif n_of_sticks > 0: 
            print('There are',n_of_sticks,'sticks in the pile.\n')
        indicator = 'user'    
        return indicator ,n_of_sticks
    
def bot_take_stick (n_of_sticks, take_not_more_than = 2, winner_condition = 1):
    
    taken_pattern = winner_condition + take_not_more_than
    stick_left = ((n_of_sticks // taken_pattern)*taken_pattern) + winner_condition
    
    if stick_left == n_of_sticks:
        if n_of_sticks == winner_condition:
            n_bot_take = winner_condition
        else:
            n_bot_take = random.randint(winner_condition,take_not_more_than)
    elif stick_left < n_of_sticks:
        n_bot_take = n_of_sticks - stick_left
    else:
        n_bot_take = n_of_sticks - stick_left + taken_pattern
    n_of_sticks -= n_bot_take    
    print('I take {} stick, there are {} sticks in the pile.'.format(n_bot_take,n_of_sticks))
    return n_of_sticks    
    
def winner_indicator (indicator,name):
    if indicator == 'user' :
        print('You take the last stick,\n I WON (Python WON)')
    else:
        print('I take the last stick,\n YOU WON ({} WON)'.format(name))
        




    
    


