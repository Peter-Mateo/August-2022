import os, random as rnd
clear = lambda: os.system('cls')
clear()
#Intro
print("Hello, and Welcome to Bagels! The Deductive reasoning game!!")
intro_answer = input("Are you Ready to play? Yes? No?  ").lower()
if intro_answer == "yes":
    clear()
    print(
    """
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When i say:         that means:
Pico                One digit is correct but in the wrong position.
Fermi               One digit is correct and in the right position.
Bagels              No digit is correct. 
    """)
    #Confirmation on rules
    ready_answer = input("Do you understand the rules?  ").lower()
    ## Game starts 
    if ready_answer == "yes":
        clear()
        logic_game_answer = str(rnd.randint(100,999))
        # Initializing substring
        A = 1 
        #Creating a result list
        result = []
        for i in range(0, len(logic_game_answer), A):
            #Converting to int, after the slicing process
            result.append(int(logic_game_answer[i : i + A]))
        # Prediction -
        print("""
I have thought up a number.")
What is your guess? ")
Don't forget it has to be three digits! One digit at a time plz!
        """)
        guess = [int(input()),int(input()),int(input())]
        guess_count = 1 
        # Set number of chances
        try_counter = 1
        # Declare list
        list_guess = [-1,-1,-1]
        for i in range(len(result)):
            if guess[0] == result[i]:
                if 0 != i:
                    list_guess[0] = (f"{guess[0]} Pico")
                elif 0 == i:
                    list_guess[0] = (f"{guess[0]} Fermi")
            elif guess[1] == result[i]:
                if 1 != i:
                    list_guess[1] = (f"{guess[1]} Pico")
                elif 1 == i:
                    list_guess[1] = (f"{guess[1]} Fermi")
            elif guess[2] == result[i]:
                if 2 != i:
                    list_guess[2] = (f"{guess[2]} Pico")
                elif 2 == i:
                    list_guess[2] = (f"{guess[2]} Fermi")
        clear()
        # Start of Loop 
        while guess != result:
            if try_counter == 11:
                break
            clear()
            print("-"* 15)
            if list_guess == [-1,-1,-1]:
                print(f"{guess} Bagels")
            elif -1 in list_guess:
                list_guess.remove(-1)
                if -1 not in list_guess:
                    print(f"{list_guess}")
                elif -1 in list_guess:
                    list_guess.remove(-1)
                    if -1 not in list_guess:
                        print(f"{list_guess}")
                    elif -1 in list_guess:
                        list_guess.remove(-1)
                        if list_guess == []:
                            print(f"{list_guess}")
            print(f"""
Guess number: {guess_count}
Your last Guess: {guess}
What is your next guess?
Don't forget it has to be three digits!
            """)
            guess = [int(input()),int(input()),int(input())]
            if guess == result:
                clear()
                print("Your Guess was Spot on!!!")
                print("You have Won!")
                print(f"The right numbers were {result}")
                reply = input("To close, type 'close':  ").lower()
                if reply == "close":
                    clear()
                    quit()
            else:
                list_guess = [-1,-1,-1]
                for i in range(len(result)):
                    if guess[0] == result[i]:
                        if 0 != i:
                            list_guess[0] = (f"{guess[0]} Pico")
                        elif 0 == i:
                            list_guess[0] = (f"{guess[0]} Fermi")
                    elif guess[1] == result[i]:
                        if 1 != i:
                            list_guess[1] = (f"{guess[1]} Pico")
                        elif 1 == i:
                            list_guess[1] = (f"{guess[1]} Fermi")
                    elif guess[2] == result[i]:
                        if 2 != i:
                            list_guess[2] = (f"{guess[2]} Pico")
                        elif 2 == i:
                            list_guess[2] = (f"{guess[2]} Fermi")
            try_counter += 1
            guess_count += 1
        clear()
        print(f"""                
                You   have hit past the 10th try mark, Try again!
                The correct number was {result}""")
# If you choose to not play game
else:
    clear()
    close = input("To close the program, type 'close':  ").lower()
    if close == "close":
        clear()
        quit()

