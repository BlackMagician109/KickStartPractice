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
totalCandy = 0  #Total number of candies in all the bags
remainingCandy = 0  #Candies remaining after the distribution
ans = []    #Final answer of the program

#Inputs
line1 = input() #Line 1 of the input
testCases = int(line1)
for i in range(testCases):
    line2 = input().split()
    bags = int(line2[0])
    kids = int(line2[1])

    candiesInBag = input().split()

    for i in candiesInBag:
        candy.append(int(i))
    
    for i in candy:
        totalCandy += i

    
    remainingCandy = totalCandy % kids
    ans.append(remainingCandy)
    #Emptying the variables for the next itteration of the loop
    totalCandy = 0
    candy = []

for i in ans:
    print("Case #" + str(ans.index(i)+1) + ": " + str(i))