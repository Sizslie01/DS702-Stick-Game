#MID-Term exam 2
#23/8/2023
#Tanasin Sriwichai
def count_5 (string):
    #Create function to identify and count number 5 in binary form (101) from the binary input
    #by receive binary as string.
    count = 0
    for i in range(0,len(string)-2):#loop for lenght of string times to check each position for 3 position 
                                    #in 1 postion that start from 0 such as [0,1,2] , [1,2,3] , .....
            count = count + 1 if string[i:i+3] == '101' else count + 0#count + 1 if the program found '101' in the string
    return count #return count from function

s = input('Enter the binary string: ') #input binary as string
count_binary_5 = count_5(s) #call count number 5 function
print('The number \'5\' value substring is: {}'.format(count_binary_5)) #display count of '101'      