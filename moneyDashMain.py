import textGraphics as tg
from getMoney import getRandomNumber as gmRand
from getMoney import getPlayerPick as gmPlayPick
import instructions
#from getMoney import whichIsGreater as gmW
#import pickANumber4 as pickAN
import os
os.system('cls')

tg.grabUserName()
instructions.rules()
# tg.graphicHello()
# tg.sayHELLO()
computerPick = gmRand()
computerPick = int(computerPick[0])
playerPick = gmPlayPick()
# playerPick = int (playerPick)

bank = 0
bank = int(bank)
#d = getRandomNumber()
while (playerPick != computerPick):
    bank = int(bank + 250000)
    print('You picked: {}, Computer picked:{}. You have ${} in the bank\n'.format(playerPick, computerPick, bank))
    print('You survived! Try again!')
    computerPick = gmRand()
    computerPick = int(computerPick[0])
    playerPick = gmPlayPick()
    # playerPick = int (playerPick)
print('Game over! You matched with the Computer. You picked: {}, Computer picked:{}.\n'.format(playerPick, computerPick))

if (bank >= 1000000):
    # print('You picked: {}, Computer picked:{}'.format(playerPick, computerPick, bank))
    print('\nJackpot!!! You get to keep your money since you\'ve made over $1 Million. Rejoice in your earnings! ${}\n'.format(bank))
else:
    # print('You picked: {}, Computer picked:{}'.format(playerPick, computerPick, bank))
    print('\nWomp-Womp!!! You matched with the Computer before reaching $1M. You had earned ${}, but you leave with ${}.\n'.format(bank, bank-bank))

# print('Game Over! Two random numbers: {}, {}. You have ${} in the bank'.format(d[0], d[1], bank))







#gmW(first = a, second = b)


# getUserName = input('Enter User Name: ')
# os.system('cls')
# tg.graphicHello(getUserName)
# if __name__ == "__main__":
#     main()
