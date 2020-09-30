#Imports
import random

#Variables
pot = 100

#Game of HEADS or TAILS 
def coin_flip(): 
    result = random.randint(0, 1)
    if result == 1:
        return "Heads"
    else:    
        return "Tails"

def heads_or_tails(wager):
    global pot
    player_guess = input("Heads or Tails? (h/t) - ")
    if player_guess == "h":
        print('You guessed heads')
    elif player_guess == "t":
        print('You guessed tails') 

    result = coin_flip()

    #result = HEADS
    if result == "Heads":
        if player_guess == "h":
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('You win! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager) 
            print('You have lost, your pot is now £' + str(pot))

    #result = TAILS
    if result == "Tails":
        if player_guess == "t":
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('You win! Your pot is now £' +str(pot))
        else:
            pot = pot - int(wager) 
            print('You have lost, your pot is now £' + str(pot)) 


#Game of CHO_CHAN
def dice_roll():
    dice_1_roll = random.randint(1, 6)
    dice_2_roll = random.randint(1, 6)
    rolled_result = dice_1_roll + dice_2_roll
    if rolled_result % 2 == 0:
        return 'e'
    else:
        return 'o'

def cho_chan(wager):
    global pot
    prediction = input('Odd or Even? (o/e) - ')
    if prediction == 'e':
        print('You guessed Even')
    elif prediction == 'o':
        print('You guessed Odd')
    #Results   
    if prediction == dice_roll():
        winnings = int(wager) * 2
        pot += int(winnings) + int(wager) 
        print('You guessed correctly!')
        print('You win! Your pot is now £' + str(pot)) 
    elif prediction != dice_roll():
        pot = pot - int(wager) 
        print('You have lost, your pot is now £' + str(pot))

#Game of HIGHEST CARD WINS
def card_choice(wager):
    global pot
    #Card generated
    deck = [1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King',] * 4
    player1_choice = deck[random.randint(0,len(deck))-1]
    player2_choice = deck[random.randint(0,len(deck))-1]
    
    jqk_list = ('Jack', 'Queen', 'King')

    #Player guesses
    input('Pick a card player 1 (Press Enter)')
    print('Player 1 your card is ' + str(player1_choice))
    
    input(
        '''Now Computer. 
            
 Hey man, I'm computer, a little help? -> (Press Enter)''')
    print('My card is ' + str(player2_choice))
    

    #Comparing face cards
    if player1_choice in jqk_list == player2_choice:
        print('Its a draw! Noone wins, you can have your money back.')
    elif player1_choice == 'King' or player2_choice == 'King':
        if player1_choice == 'King':
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager) 
            print('Player 1 Wins! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager)
            print('I Win, sorry man your pot is now £' + str(pot))
    elif player1_choice == 'Queen' or player2_choice == 'Queen':
        if player1_choice == 'Queen' and player2_choice == 'Jack':
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('Player 1 Wins! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager)
            print('I Win, sorry man your pot is now £' + str(pot))
    elif player1_choice == 'Jack' or player2_choice == 'Jack':
        if player1_choice == 'Jack' and player2_choice <= 10:
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('Player 1 Wins! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager)
            print('I Win, sorry man your pot is now £' + str(pot))

    #For head cards higher than numbers
    elif player1_choice in jqk_list and player2_choice <= 10:
        winnings = int(wager) * 2
        pot += int(winnings) + int(wager)
        print('Player 1 Wins! Your pot is now £' + str(pot))
    elif player2_choice in jqk_list and player1_choice <= 10:
        pot = pot - int(wager)
        print('I Win, sorry man your pot is now £' + str(pot))
    
    #Comparing if both cards are numbers
    elif player1_choice == player2_choice:
        print('Its a draw no one wins, you can have your money back.')
    elif player1_choice > player2_choice:
        winnings = int(wager) * 2
        pot += int(winnings) + int(wager)
        print('Player 1 Wins! Your pot is now £' + str(pot))    
    else:
        pot = pot - int(wager)
        print('I Win, sorry man your pot is now £' + str(pot))


#Game of semi Roulette
def roulette(wager):
    global pot
    #Players choice
    players_choice = input('''
    You can bet on:
     - Any number (Enter a number)
     - Numbers between 1-18 or 19-36 (1-18 = l 19-36 = h)
     - Odds or Evens (Odd = o Even = e)    
    ''')
    #Numbers between 1-18 or 19-36
    if players_choice == 'l' or players_choice == 'h':
        if players_choice == 'l':
            print('Your choice is LOWER')
        else:
            print('Your choise is HIGHER')
    elif players_choice == 'o' or players_choice == 'e':
        if players_choice == 'o':
            print('Your choice is ODDS')
        else:
            print('Your choice is EVENS')
    elif int(players_choice) > 36 or int(players_choice) < 0:
        print('This number is not in the range of what you can select!')
        players_choice = input('Please select another number - ')
    else:
        print('Your choice is ' + str(players_choice))

    #Spin the wheel
    wheel_numbers = random.randint(0, 36)
    print('The ball landed on ' + str(wheel_numbers))

    #Result
    if players_choice == 'l':
        if players_choice == 'l' and wheel_numbers in range(0, 19):
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('You win! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager)
            print('You lose! Your pot is now £' + str(pot))

    elif players_choice == 'h':
        if players_choice == 'h' and wheel_numbers in range(19, 37):
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('You win! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager)
            print('You lose! Your pot is now £' + str(pot))

    elif players_choice == 'o':
        if players_choice == 'o' and wheel_numbers % 2 == 1:
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('You win! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager)
            print('You lose! Your pot is now £' + str(pot))

    elif players_choice == 'e':
        if players_choice == 'e' and wheel_numbers % 2 == 0:
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('You win! Your pot is now £' + str(pot))
        else:
            pot = pot - int(wager)
            print('You lose! Your pot is now £' + str(pot))

    else:
        if players_choice != wheel_numbers:
            pot = pot - int(wager)
            print('You lose! Your pot is now £' + str(pot))
        else:
            winnings = int(wager) * 2
            pot += int(winnings) + int(wager)
            print('You win! Your pot is now £' + str(pot))

#Master code that will be revisited each a game is played and to select the new game if they have the correct money.    
def game_play():
    global pot    
    if pot > 0:
        print('You have £' + str(pot))
        print()
        game_choice = input(
                '''What game would you like to play?
    - Heads & Tails (ht)
    - Cho Chan (cc)
    - Highest Card (hc)
    - Semi Roulette (sr)

    Game - '''            
        )
        print(
            'How much would you like to wager?'
        )
        wager = input('£')
        if int(wager) > pot:
            print('You dont have enough money to play, please place another wager')
            wager += input('£')
        chosen_game(game_choice, wager)
        play_again = input('Play another game? Y/N - ')
        if play_again == 'Y':
            game_play()
        elif play_again == 'N':
            print('Thanks for playing your winnings are £' + str(pot) + ' was it worth it?')
    elif pot < 0:
        print('You do not have enough monney to play! Do not add more go home to your wife and kids')

def chosen_game(game_choice, wager):
    if game_choice == 'ht':
        heads_or_tails(wager)
    elif game_choice == 'cc':
        cho_chan(wager)
    elif game_choice == 'hc':
        card_choice(wager)
    else:
        roulette(wager)


game_play()

