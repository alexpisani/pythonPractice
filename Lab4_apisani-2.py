# Lab4_apisani-2.py
# Alex Pisani
# June 10 2024
# a simple hangman guessing game

import random

magic_number = random.randint(1,15)
hanged_list = [""" O """,
               """/|\\ """,
               """/\\ """]
guess = 0
game_over = False
play_again = True

while play_again:
    while not game_over:
        user_number = ''
        if guess == 0:
            user_number = input("Please guess a number from 1 to 15 (Steve's life depends on this...) ")
        else:
            user_number = input("Please guess another number from 1 to 15 ")
        
        while (not user_number.isnumeric()) or (int(user_number) >15) or (int(user_number) <1):
            user_number = input("Please guess from 1 to 15: ")

        guess += 1
            
        if int(user_number) == magic_number:
            print ("Congratulations! Steve can return home to his numerous children!")
            game_over = True
            play_again = input("Would you like to play again? enter y/n: ").lower().startswith('y')
            if not play_again:
                print ("GAME OVER - THANKS FOR PLAYING!")
                   
        elif guess == len(hanged_list):
            print ('\n'.join(hanged_list[:guess]))
            print ("Steve has died an ignominious death, are you happy?")
            game_over = True
            play_again = input("Would you like to play again? enter y/n: ").lower().startswith('y')
            if not play_again:
                print ("GAME OVER - THANKS FOR PLAYING!")
           
        else:
            print ('\n'.join(hanged_list[:guess]))

    game_over = False
    guess = 0