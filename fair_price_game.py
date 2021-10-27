import random

def fair_price():
    answer=random.randint(0,200)
    print(answer)
    while True:
        guess=int(input('\nGuess:'))
        if guess>answer:
            print('Too high')
        elif guess<answer:
            print('Too small')
        else:
            print('\nyou win little piece of shit')
            break
    if str(input('\nReplay? (y/n)'))=='y':
        fair_price()
    else:
        False
        #pass

if __name__=='__main__':
    fair_price()
