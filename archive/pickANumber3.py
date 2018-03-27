import random
import os
import sys

os.system('cls')
# def pickANumber():
#     pickUsersNumber = int(input("Enter a number between 1 and 15: "))
#     print(pickUsersNumber)
#     return pickUsersNumber
#
def getRandomNumber():
    getRandomInt = random.randint(1,15)
    getRandomInt2 = random.randint(1,15)
    #print(getRandomInt,getRandomInt2)
    return getRandomInt, getRandomInt2

# a = getRandomInt()
# print(a)


#proof of concept for assigning function to a variable.
a = getRandomNumber()
print('Two random numbers:{}, {}'.format(a[0],a[1]))




#testing for whichIsGreater
b = input("Enter 1st Number:")
c = input("Enter 2nd Number:")

def whichIsGreater(first, second):
    if first > second:
        print('First number {} is greater than second number {}'.format(first,second))
    elif first == second:
        print('Your numbers are equal: {},{}'.format(first,second))
    else:
        print('Second number {} is greater than first number {}'.format(second, first))

whichIsGreater(first = b, second = c)
