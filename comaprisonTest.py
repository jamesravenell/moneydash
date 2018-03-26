import os
os.system('cls')


# manNum =int(0)
# while True:
#     manNum <= 200
#     print(manNum)
#     manNum = manNum + 10


# bread = 35
# while bread >= 2:
#     print("I'm making a sandwich")
#     bread = bread - 2


zeroQuit = list()
print('Enter intergers, one per line. Type 0 to quit:')
userInput = 1
while userInput != 0:
    zeroQuit.append(userInput)
    userInput = input('Enter another number:')
    userInput = int(userInput)
print('You entered 0, game over!')
