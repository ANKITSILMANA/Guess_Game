###########################################################GUESS GAME############################################
import random
n = random.randint(0,20)
print("\t\t\t\t\t\t\t\t###########             #####         #####   ###########    ###########    ########### ")
print("\t\t\t\t\t\t\t\t###########             #####         #####   ###########    ###########    ########### ")
print("\t\t\t\t\t\t\t\t####                    #####         #####   ####           ###            ###         ")
print("\t\t\t\t\t\t\t\t####                    #####         #####   ####           ###            ###         ")
print("\t\t\t\t\t\t\t\t####      ###########   #####         #####   ##########     ###########    ########### ")
print("\t\t\t\t\t\t\t\t####      ###########   #####         #####   ##########     ###########    ########### ")
print("\t\t\t\t\t\t\t\t####      ####    ###   #####         #####   ####                   ###            ### ")
print("\t\t\t\t\t\t\t\t##############    ###   ###################   ###########            ###            ### ")
print("\t\t\t\t\t\t\t\t##############    ###   ###################   ###########    ###########    ########### ")
print("You have Total 9 guesses\n")
g = 9
Y = str("Y")
C = str("C")
y = str("y")
c = str("c")
while ( True ) :
    try:
        # n=18
        a = int(input("Enter number\n"))
        g = g - 1
        print("Please Enter Smaller Number") if a > n else print("Please Enter Greater Number") #This is one line statement
        # if a > n:
        #     print("Please Enter Smaller Number")
        # else:
        #     print("Please Enter Greater Number")

        if g == 0:
            print("Game Over!\n")
            print("DO YOU WANT TO PLAY AGAIN\n"
                  "PRESS Y FOR PLAY\n"
                  "PRESS C for EXIT")
            p = input()
            if p==int:
                break
            elif p == Y or p == y :
                g = 9
                n = random.randint(0, 20)
                continue
            elif p == C or p == c or p!=int:
                break
        elif a != n:
            print("No.of Guesses Left", g, "\n")
            continue

        elif a == n:
            print("Conograts!YOU WON\n")
            print("You have",g,"guesses Left\n")
            print("You Take only",9-g,"guesses\n")
            print("DO YOU WANT TO PLAY AGAIN\n"
                  "PRESS Y FOR PLAY\n"
                  "PRESS C for EXIT")
            p = input()
            if p==int:
                break
            elif p == Y or p == y:
                n = random.randint(0, 20)
                g = 9
                continue
            elif p == C or p == c:
                break
    except Exception as e:
        print("Invalid character")
        break
