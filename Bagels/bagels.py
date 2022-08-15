import os, random as rnd
clear = lambda: os.system('cls')
# A deductive logic Game, you must guess a secreet three- digit number based on clues. the game offers one of the following hints in response to your guess: "Pico" when your guess has a correct digit in the wrong place, "Fermi" when your guess has a correct digit in the correct place, and "Bagels" if your guess has no correct digits. You have 10 tries to guess the secret number 
clear()
print("Hello, and Welcome to Bagels! The Deductive reasoning game!!")
intro_answer = input("Are you Ready to play? Yes? No?  ").lower()
if intro_answer == "yes":
    clear()
    print("There are three digits that you must guess, with the given clues. You will be told when your guess has a correct digit in the correct place. You have 10 tries to guess the secret number.")
    ready_answer = input("Do you understand the rules?  ").lower()
    if ready_answer == "yes":
        logic_game_answer = rnd.randint(0,10), rnd.randint(0,10), rnd.randint(0,10)
        print(logic_game_answer)
else:
    clear()
    close = input("Would you like to close the program? Yes? No?  ").lower()
    if close == "yes":
        clear()
        quit()

