import os, random as rnd
clear = lambda: os.system('cls')
# Start of the program
while True:
    clear()
    print("""
Welcome to the deductive logic game, I will think of a three digit number in which you have to guess the correct number. 
    """)
    # Taking input to see if they want to play
    ready_q1 = input("Are you ready to play?    ").lower()
    if ready_q1 == 'yes':
        clear()
        while True:
            # Key to the game
            print("""
The game offers one of the follwing hints in response to your guess: 
When I say:         that means:
Pico                Guess is the correct digit but in the wrong place
Fermi               Correct digit in the correct place
Bagels              All three digits aren't any of the numbers I was thinking of    
    """)
            # Understanding of the rules
            understand_rules = input("Do you understand these rules? We will also leave the key at the top of the screen in case you forget them!").lower()
            if understand_rules == 'yes':
                # Start of the program - Creates 3 digit number
                three_digit_number = str(rnd.randint(100,999))
                # Game count
                guess_count = 0
                # Slicing integers 
                sliced_first_digit = three_digit_number[:1]
                sliced_second_digit = three_digit_number[1::3]
                sliced_third_digit = three_digit_number[2::]
                # Creating list to hold the answer
                answer_list = [sliced_first_digit, sliced_second_digit, sliced_third_digit]
                while True:
                    if guess_count != 0:
                        print(f"Guess: #{guess_count}")
                    question = input("""
I am thinking of a three-digit number.
What number do you think it is?
""")        
                    # Slicing integers
                    question_first_digit = question[:1]
                    question_second_digit = question[1::3]
                    question_third_digit = question[2::]
                    # Creating list to hold Key Value pairs
                    numb = [0,0,0]
                    for i in range(len(three_digit_number)):
                        if question_first_digit == answer_list[i]:
                            if 0 == answer_list[i].index:
                                numb.insert(f"Fermi, {question_first_digit}", 0)
                            else:
                                numb.insert(f"Pico, {question_first_digit}", 0)
                        if question_second_digit == answer_list[i]:
                            if 1 == answer_list[i].index:
                                numb.insert(f"Fermi, {question_first_digit}", 1)
                            else:
                                numb.insert(f"Pico, {question_first_digit}", 1)
                        if question_third_digit == answer_list[i]:
                            if 2 == answer_list[i].index:
                                numb.insert(f"Fermi, {question_first_digit}", 2)
                            else:
                                numb.insert(f"Pico, {question_first_digit}", 2)
                    quit()
            else:
                clear()
                close = input("If you would like to close the game, you can by typing 'close' ").lower()
                if close == 'close':
                    quit()
                else:
                    clear()
                    continue
    else:
        clear()
        close = input("If you would like to close the game, you can by typing 'close' ").lower()
        if close == 'close':
            quit()