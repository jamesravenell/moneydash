import random
import os
import sys

os.system('cls')
# def pickANumber():
#     pickUsersNumber = int(input("Enter a number between 1 and 15: "))
#     print(pickUsersNumber)
#     return pickUsersNumber
#
# def getRandomNumber():
#     getRandomInt = random.randint(1,15)
#     print(getRandomInt)
#     return getRandomInt

#testarea
# pickUsersNumber = int(input("Enter a number between 1 and 10: "))
# print('You selected:{}'.format(pickUsersNumber))
# getRandomInt = random.randint(1,10)
# print('Computer picks:{} '.format(getRandomInt))
#
# if pickUsersNumber == getRandomInt:
#     print('You lose, Sucka!')
# else:
#     print('You live to play again!')

pickUsersNumber = 0
getRandomInt = 0

def whatsTheNumber():
    pickUsersNumber = int(input("Enter a number between 1 and 10: "))
    print('You selected:{}'.format(pickUsersNumber))
    getRandomInt = random.randint(1,10)
    print('Computer picks:{} '.format(getRandomInt))
    return(pickUsersNumber,getRandomInt)
#
# def compareNumbers(playerSelection, computerSelection):
#     while playerSelection != computerSelection:
#         print('You live to play again!')
#     else:
#         print('You lose, Sucka from compare!')

# call the function
whatsTheNumber()
print(pickUsersNumber)
# compareNumbers(whatsTheNumber(),whatsTheNumber())
# compareNumbers(playerSelection = pickUsersNumber, computerSelection = getRandomInt)


#print('You lose, Sucka!')




# pickANumber()
# getRandomNumber()

# if a == b:
#     print('You lose!')
# else:
#     print('Woohoo')
