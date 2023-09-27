#MID-Term exam 1
#23/8/2023
#Tanasin Sriwichai
import numpy as np
n = int(input('Input the size of square metrix (N):')) #Input size of square metrix
A = np.ones((n,n)) #create array of number "1" for N*N size
for i in range(n): #Loop in range of row
    for j in range(n): #Loop in range of column
        if i < j: #if index row less than column a[i,j] = i+j
            A[i,j] = i+j
        elif i > j:#if index row more than column a[i,j] = i-j
            A[i,j] = i-j
print(A)#Display metrix A