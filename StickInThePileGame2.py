n_stick = int(input('How many sticks (N) in the pile:'))
print('There are',n_stick,'sticks in the pile.')
name = input('What is your name: ')

times = 0
while n_stick > 0:
    
    n_out = int(input('{}, how many sticks you will take (1 or 2):'.format(name)))
    
    if n_out > 2: #1st condition check the limit number of taken stick and amount of stick left.
        print('No you cannot take more than 2 sticks!')
    elif n_out < 1:
        print('No you cannot take less than 1 stick!')
    elif n_out > n_stick:
        print('There are no enough sticks to take.')
    else :
        n_stick -= n_out #take the stick from the pile.
        times += 1 #count times of taken stick.
        if n_stick > 0: #2nd condition check the number of stick left in the pile and told the user. 
            print('There are',n_stick,'sticks in the pile.')
            
    
    
    
print('OK. There is no stick left in the pile. You spend',times,'times.')