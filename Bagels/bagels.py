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
    if ready_answer == "yes": ## Game starts 
        clear()
        logic_game_answer = str(rnd.randint(100,999))
        # Initializing substring
        A = 1 
        #Creating a result list
        result = []
        for i in range(0, len(logic_game_answer), A):
            #Converting to int, after the slicing process
            result.append(int(logic_game_answer[i : i + A]))
        print(result)
        print("What is your first guess? ")
        print("Don't forget it has to be three digits!")
        guess = (int(input()),int(input()),int(input()))
        if guess == logic_game_answer:
            print("Your Guess was Spot on!!!")
            print("You have Won!")
            replay = input("Would you like to play again?  ").lower()
            if replay == "yes":
                pass
        else:
            pass
else:
    clear()
    close = input("Would you like to close the program? Yes? No?  ").lower()
    if close == "yes":
        clear()
        quit()

