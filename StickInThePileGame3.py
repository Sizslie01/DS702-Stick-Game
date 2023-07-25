#660631097 Tanasin Sriwichai
#HW1E_stickpile
#26-7-2023
import random

name = input('What is your name : ')
n_sticks = int(input('How many sticks (N) in the pile: '))
print('There are {} sticks in the pile'.format(n_sticks))


#stick_taken = int(input('How many stick can be taken: '))
#winner_taken = int(input('How many number of last will be lose: '))

#Note 
def user_take_stick (n_of_sticks, take_not_more_than = 2, winner_condition = 1):
    #Define the action of user and display result from following condition.
    while n_of_sticks > 0:
        n_take = int(input('How many you will take (1 or 2): '))
        if n_take > take_not_more_than: #1st condition check the limit number of taken stick and amount of stick left.
            print('No you cannot take more than {} sticks!'.format(take_not_more_than))
        elif n_take < winner_condition:
            print('No you cannot take less than {} stick!'.format(winner_condition))
        elif n_take > n_of_sticks:
            print('There are no enough sticks to take.')
        else:
            n_of_sticks -= n_take
            if n_of_sticks == winner_condition:#2nd condition check how many stick left after taken out.
                print('There are',n_of_sticks,'stick in the pile.\n')
            elif n_of_sticks > 0: 
                print('There are',n_of_sticks,'sticks in the pile.\n')
            loser = 'user' #Check who pick the stick now!
            return loser ,n_of_sticks
    
def bot_take_stick (n_of_sticks, take_not_more_than = 2, winner_condition = 1):
    #Define the action of bot and display result from following condition.
    taken_pattern = winner_condition + take_not_more_than #check the winnable pattern.
    
    stick_left = ((n_of_sticks // taken_pattern)*taken_pattern) + winner_condition 
    if stick_left == n_of_sticks: #Check how many stick should be left.
        if n_of_sticks == winner_condition:
            n_bot_take = winner_condition
        else:
            n_bot_take = random.randint(winner_condition,take_not_more_than)
    elif stick_left < n_of_sticks:
        n_bot_take = n_of_sticks - stick_left
    else:
        n_bot_take = n_of_sticks - stick_left + taken_pattern

    n_of_sticks -= n_bot_take    #take the stick.
    print('I take {} stick, there are {} sticks in the pile.'.format(n_bot_take,n_of_sticks))
    loser = 'bot' #Check who pick the stick now!
    return loser ,n_of_sticks    
    
def winner_indicator (loser,user_name): #Display the winner from loser_indicator.
    if loser == 'user' :
        print('You take the last stick,\nI WON (Python WON)')
    else:
        print('I take the last stick,\nYOU WON ({} WON)'.format(user_name))
        
#Calling main funtion.
while n_sticks > 0: 
    indicator ,n_sticks = bot_take_stick(n_sticks)
    if n_sticks > 0:
        indicator ,n_sticks = user_take_stick(n_sticks)

winner_indicator (indicator,name)




    
    


