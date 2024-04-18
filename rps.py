import random

game = True

rps = ["rock", "paper", "scissors"]

while game:

    user = input("\nPlease enter: \nRock 👊 \nPaper 🖐\nScissors ✌\n\n").lower()

    python = random.choice(rps)

    if user not in rps: 
        print("\nNot a valid Answer try again!")
    elif user == python:
        print("\nIt's a tie!")
    elif user == rps[0] and python == rps[2]:
        print("\nYou win! 😎")
    elif user == rps[1] and python == rps[0]:
        print("\nYou win! 😎")
    elif user == rps [2] and python == rps[1]:
        print("\nYou win! 😎")
    else:
        print("\nPython Wins 🐍")

    print(f"\nYou picked {user} and Python picked {python}\n")



    # First iteration of replay loop

    # if replay.lower() == "y":
    #     continue
    # else:
    #     game = False
    #     print("Thank you for playing! 😘")
    
    
    game_replay = True

    while game_replay:

        replay = input('Would you like to play again? \n"Y" for yes \n"Q" for no\n\n')

        if replay.lower() == "y":
            break
        elif replay.lower() == "q":
            print("\nThank you for playing!")
            game = False
            game_replay = False
        else:
            print('\nInvalid input!')
            continue
         
    continue