# import os
# os.system('cls')
import time

'''let's add some color'''
CRED = '\033[91m'
CUND = '\033[04m'
CWHO = '\033[94m'
CBGR = '\033[40m'
CEND = '\033[0m'

def makeSpaces():
    print('\n\n\n')#just making output clearer

def sayHI():
    print('***   ***   ***  ***')
    print('***   ***   ***  ***')
    print('***   ***   ***  ***')
    print('*********   ***  ***')
    print('***   ***   ***  ***')
    print('***   ***   ***   - ')
    print('***   ***   ***  ***')
    print('\n\n')

def hashLine67():
    print('\t{}'.format(''.center(67,'#')))

def sayHELLO():
    print('\n')
    print('\t###     ###    #########    ###       ###       ############   ####')
    print('\t###     ###    ##           ###       ###       ############   ####')
    print('\t###     ###    ##           ###       ###       ###      ###   ####')
    print('\t###########    ######       ###       ###       ###      ###   ####')
    print('\t###     ###    ##           ###       ###       ###      ###   ####')
    print('\t###     ###    ##           #######   #######   ############    ** ')
    print('\t###     ###    #########    #######   #######   ############   ####')
    print('\n')

def graphicHello (user):
    makeSpaces()
    hashLine67()
    hashLine67()
    sayHELLO() #BIG HELLO
    hashLine67()
    hashLine67()
    print('\t'+ CRED+CBGR +'{}'.format(user.center(67,' ')))  #will print centered username w/a '#' or ' ' surrounding
    print('\t'+ CEND +'{} '.format(''.center(67,'#')))
    hashLine67()
    makeSpaces()
    time.sleep(3)
    # os.system('pause')

'''
I didn't NEED the grabUserName function. Instead of deleting the code,
I just put the pertinent functionality into a function in case i might need it later.
However, it MUST follow the graphicHello function.
'''

def grabUserName():
    getUserName = input('Enter User Name: ')
    # os.system('cls')
    graphicHello(getUserName)
    # return getUserName


if __name__ == "__main__":
    main()
