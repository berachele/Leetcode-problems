import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #create dictionary to match pairs
    #create integar value to count pairs
    #loop through array:
        #if number not already in dictionary, add it's number as value, and 0 as starting count
        #add 1 to the count
        #check if dictionary is equal to 2 (meaning one pair is made)
            #if there is, add one to results and restart dict[i] at 0
    #return results
    
    dict = {}
    results = 0

    for i in ar:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
        if dict[i] == 2:
            results += 1
            dict[i] = 0

    return results

#Testing
n = 9
myArray = [10, 20 , 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(n, myArray))