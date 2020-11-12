"""Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock

Input Format
The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.
 
Output Format
Return the total number of matching pairs of socks that Alex can sell.""

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
