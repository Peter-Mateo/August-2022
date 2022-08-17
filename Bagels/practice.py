import os, random as rnd
clear = lambda: os.system('cls')

clear()
print("""
Welcome to the deductive logic game, I will think of a three digit number in which you have to guess the correct number. 
""")
ready_q1 = input("Are you ready to play?    ").lower()
if ready_q1 == 'yes':
    clear()
    while True:
        print("""
The game offers one of the follwing hints in response to your guess: 
When I say:         that means:
Pico                Guess is the correct digit but in the wrong place
Fermi               Correct digit in the correct place
Bagels              All three digits aren't any of the numbers I was thinking of    
""")
        understand_rules = input("Do you understand these rules? We will also leave the key at the top of the screen in case you forget them!")
        if understand_rules == 'yes':
            break
        else:
            close = input("If you would like to close the game, you can by typing 'close' ").lower()
            if close == 'close':
                quit()
            else:
                continue
