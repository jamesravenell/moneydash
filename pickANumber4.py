import random
import os
import sys
import textGraphics

os.system('cls')

#this just grabs 2 random numbers and returns them when the function is called
def getRandomNumber():
    getRandomInt = random.randint(1,100)
    getRandomInt2 = random.randint(1,100)
    #print(getRandomInt,getRandomInt2)
    return getRandomInt, getRandomInt2


#proof of concept for assigning function to a variable.
# a = getRandomNumber()
# print('Two random numbers:{}, {}'.format(a[0],a[1]))


#This function checks to see which of 2 INT are greater
def whichIsGreater(first, second):
    if first > second:
        print('First number {} is greater than second number {}'.format(first,second))
    elif first == second:
        print('Your numbers are equal: {},{}'.format(first,second))
    else:
        print('Second number {} is greater than first number {}'.format(second, first))


#testing for whichIsGreater
# b = input("Enter 1st Number:")
# c = input("Enter 2nd Number:")

#this uses two numbers entered
# whichIsGreater(first = b, second = c)

#works
# textGraphics.makeSpaces()
# textGraphics.graphicHello(user=input('What\'s your username?:'))

#works
# whichIsGreater(first = a[0], second = a[1])

'''
need a while loop to test if numbers equal
if not, repeat the loop.
'''
bank = 0
d = getRandomNumber()
while d[0] != d[1]:
    bank += 50000
    print('Two random numbers: {}, {}. You have ${} in the bank'.format(d[0], d[1], bank))
    d = getRandomNumber()
print('Game Over! Two random numbers: {}, {}. You have ${} in the bank'.format(d[0], d[1], bank))
