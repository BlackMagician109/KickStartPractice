#Coding Practice with Kick Start Session #2 - Kick Start 2022
#
#Sample Problem(1pts)
#
#Input: First line gives number of test cases
#       Each test case consists of 2 lines
#           first line of each test case contains 2 integers: The number of candy bags and the number of kids
#           the next line contains the number of candies in each bag
#
#Output: Contains one line
#           Case #x: y, where x is the test case number and y is the number of candies remaining at the end
#

#Variables
testCases = 0  #Total number of test cases
bags = 0    #Total Number of Bags
kids = 0    #Total Number of kids
candy = []  #Total number of candy in each bag


#Inputs
line1 = input() #Line 1 of the input
line2 = input.split()

testCases = int(line1)
bags = line2[0]
kids = line2[1]


candiesInBag = input().split()

for i in candiesInBag:
    candy.append(int(i))

totalCandy = 0  #Total number of candies in all the bags
remainingCandy = 0  #Candies remaining after the distribution

for i in candy:
    totalCandy += i

for i in range(testCases):
    remainingCandy = totalCandy % kids

    print("Case #i: " + remainingCandy)