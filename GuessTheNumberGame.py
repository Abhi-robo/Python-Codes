import random

print("Welcome to \'GUESStheNUMBER\' game")
numberExceed = 20 # to adjust the range of the game
def rep():
    y = 'y'
    n = 'n'
    print("do u want to play again [Y/N]")
    play = input()
    if play == y.lower() or  play  == y.upper():
        replay()
    else:
        print("thanks for playing")
def replay ():
    mynum = random.randint(1,numberExceed)
    #print(mynum)  #To know the randomNumber of the game
    guesscount = 0
    while(True):

        Instruction = "Guess my number between 0 - {}: ".format(numberExceed)
        print(Instruction)
        try:
            num = int(input())
            guesscount = guesscount + 1
            if num>= numberExceed :
                print("your choice is exceeded")
                rep()
                break
            elif guesscount >=9:
                print("Sorry your guess limit is OVER")
                print("GAME OVER")
                rep()
                break
            print(" Attempt guesses is:", guesscount)
            if num == mynum:
                print("\t You WON the GAME, and the number is", mynum)
                rep()
                break
            elif num >= (0.8*mynum ) and num<= mynum :
                print("\t\t\t you r close: guess higher than this ",num)
            elif num>=mynum and num<= 1.2*mynum :
                print("\t\t\t you r close: guess lower than this ", num)
            elif num>mynum:
                print("\t\t\t your guess was too high: guess lower than this ",num)
            elif num<mynum:
                print("\t\t\t your guess was too low: guess higher than this ",num)
        except:
            print("Please Enter the Valid Number Input")
            print()
            replay()


replay()