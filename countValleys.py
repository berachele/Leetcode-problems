"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example
steps = 8 
path = [DDUUUUDD]
The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.

Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

int steps: the number of steps on the hike
string path: a string describing the path
Returns

int: the number of valleys traversed
Input Format

The first line contains an integer , the number of steps in the hike.
The second line contains a single string , of  characters that describe the path.
"""

# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    
    #int value for sea level
    #int for counting valleys
    #loop through each char in string
        #if char is U, increment sealevel
        #if it's D, decrement sea level
        #if sea level is at 0 AND we're going up, increment valley count

    #return valley count

    seaLevel = 0
    valleys = 0

    for char in path:
        if char == 'U':
            seaLevel += 1
        if char == 'D':
            seaLevel -= 1
        if seaLevel == 0 and char == 'U':
            valleys += 1

    return valleys


#Testing
steps = 8
path = 'UDDDUDUU'

print(countingValleys(steps, path))