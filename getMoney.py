import random
import os
import sys
import textGraphics as tg


'''
this just grabs 2 random numbers and returns them when the function is called
for the purposes of testing, I added the second random.  This provides
some flexibility. Later I'll have an easy mode (1 to 20), and hard (1 to 5)
'''
def getRandomNumber():
    getRandomInt = random.randint(1,5)
    getRandomInt2 = random.randint(1,20)
    #print(getRandomInt,getRandomInt2)
    return getRandomInt, getRandomInt2



'''
Prompts Player for their number to comparea against computer's random pick
'''
def getPlayerPick():
    #getUser = tg.grabUserName()
    # pickYourNumber = input('{}, enter a number from 1 to 100:'.format(getUser))
    pickYourNumber = input('Enter a number from 1 to 5: ')
    pickYourNumber = int(pickYourNumber)
    while not (1 <= pickYourNumber <= 5):
        print('Sorry, my friend! It appears you\'re trying to be slick.\n A number between 1 and 5 is all I\'m accepting.\nTry again!')
        pickYourNumber = input('Enter a number from 1 to 5: ')
        pickYourNumber = int(pickYourNumber)
    return pickYourNumber
