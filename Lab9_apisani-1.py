# Lab9_apisani-1.py
# Alex Pisani
# Aug 4 2024
# flips 2 coins and awards or negates a point from each player depending on the outcome

from coin import Coin 

def main():
    player1 = Coin()
    player2 = Coin()
    start_game = input("Would you like to play Coin Toss? (yes/no): ").strip().lower()
    if start_game != 'yes':
        print ("Well, FINE!")
        exit()

    while True:
        player1.toss()
        player2.toss()
        
        print(f"Player 1's coin is {player1.get_sideup()}")
        print(f"Player 2's coin is {player2.get_sideup()}")
        
        if player1.get_sideup() == player2.get_sideup():
            player1.set_amount(1)
            player2.set_amount(-1)
            print("Coins matched!")
        else:
            player1.set_amount(-1)
            player2.set_amount(1)
            print("Coins did not match.")
        
        print(f"Player 1 has {player1.get_amount()} coins.")
        print(f"Player 2 has {player2.get_amount()} coins.")
        
        continue_playing = input("Do you want to continue playing? (yes/no): ").strip().lower()
        if continue_playing != 'yes':
            print("Thanks for playing!")
            break