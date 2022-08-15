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
        one = result[0]
        two = result[1]
        three = result[2]
        print("What is your guess? ")
        print("Don't forget it has to be three digits!")
        guess = [int(input()),int(input()),int(input())]
        try_one = guess[0]
        try_two = guess[1]
        try_three = guess[2]
        try_counter = 1
        list_guess = []
        for i in range(len(result)):
            if try_one == result[i]:
                if 0 != i:
                    list_guess.insert(0, f"{try_one} Pico")
                elif 0 == i:
                    list_guess.insert(0, f"{try_one} Fermi")
            elif try_two == result[i]:
                if 1 != i:
                    list_guess.insert(1, f"{try_two} Pico")
                elif 1 == i:
                    list_guess.insert(1, f"{try_two} Fermi")
            elif try_three == result[i]:
                if 2 != i:
                    list_guess.insert(2, f"{try_three} Pico")
                elif 2 == i:
                    list_guess.insert(2, f"{try_three} Fermi")
        if list_guess == []:
            print(f"{guess} Bagels")
        clear()
        while guess != result:
            clear()
            print("-"* 15)
            print(list_guess)
            print(f"Your last Guess: {guess}")
            print("What is your next guess? ")
            print("Don't forget it has to be three digits!")
            guess = [int(input()),int(input()),int(input())]
            try_one = guess[0]
            try_two = guess[1]
            try_three = guess[2]
            if try_counter == 11:
                break
            elif guess == result:
                print("Your Guess was Spot on!!!")
                print("You have Won!")
                replay = input("Would you like to play again?  ").lower()
                if replay == "yes":
                    pass
                else:
                    clear()
                    quit()
            else:
                list_guess = []
                for i in range(len(result)):
                    if try_three == result[i]:
                        if 2 != i:
                            list_guess.insert(2, f"{try_three} Pico")
                        elif 2 == i:
                            list_guess.insert(2, f"{try_three} Fermi")
                        else:
                            attempt_1 = 'no'
                    elif try_two == result[i]:
                        if 1 != i:
                            list_guess.insert(1, f"{try_two} Pico")
                        elif 1 == i:
                            list_guess.insert(1, f"{try_two} Fermi")
                        else:
                            attempt_2 = 'no'
                    elif try_one == result[i]:
                        if 0 != i:
                            list_guess.insert(0, f"{try_one} Pico")
                        elif 0 == i:
                            list_guess.insert(0, f"{try_one} Fermi")
                        else:
                            attempt_3 = 'no'
        if list_guess == []:
            print(f"{guess} Bagels")
        try_counter += 1
        print("You have hit past the 10th try mark, Try again!")
else:
    clear()
    close = input("Would you like to close the program? Yes? No?  ").lower()
    if close == "yes":
        clear()
        quit()

