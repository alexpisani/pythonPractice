#Lab5_apisani-2.py
#Alex Pisani
#June 18 2024
# a two-player pickup-sticks game

import random
pickup = ''
stick_count = random.randint(5,20)
player1 = 'Player 1'
player2 = 'Player 2'
player_index = 0
player_list = [player1, player2]
game_over = False 
play_again = True

print ("Take turns picking up 1 to 4 sticks from the pile.\nWhoever picks up the last stick wins.\nWhy would I tell you how many sticks there are? That ruins the game!")

while play_again:
    while not game_over:       
        while stick_count > 0:
            current_player = player_list[player_index % 2]
            print (current_player)
            pickup = (input("Please pick up 1 to 4 sticks: "))
                
            while (not pickup.isnumeric()) or (int(pickup) < 1) or (int(pickup) > 4) or int(pickup) > stick_count:
                print ("You cannot take", pickup, "sticks")
                pickup = (input("Let's try a different number of sticks: "))
            stick_count -= int(pickup)
            if stick_count == 0:
                print (current_player, "wins!")
                game_over = True
                play_again = input("Would you like to play again? enter y/n: ").lower().startswith('y')
                stick_count = random.randint(5,20)
                player_index = 0
                if not play_again:
                    print ("GAME OVER - THANKS FOR PLAYING!")
                    break
            player_index += 1
    game_over = False