import random
import types
import inspect
import itertools

deck = {}
piles = []
players = []
die_roll = int
last_die_roll = int

#all the places cards can be
red_pile = {}
yellow_pile = {}
green_pile = {}
blue_pile = {}
player_1_hand = {}
player_2_hand = {}
discard_pile = {}

player_1_name = ''
player_2_name = ''
current_player = ''

colors = []
values = []
colors =  ['red', 'green', 'blue', 'yellow']
values = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

def build_deck():
    global deck
    global values
    global colors
    red = colors[0]
    green = colors[1]
    blue = colors[2]
    yellow = colors[3]
    red_cards = [[red, v] for v in zip(values)]
    green_cards = [[green, v] for v in zip(values)]
    blue_cards = [[blue, v] for v in zip(values)]
    yellow_cards = [[yellow, v] for v in zip(values)]
    deck = red_cards + green_cards + blue_cards + yellow_cards
    random.shuffle(deck)
    return values, colors, deck

def deal():
    print("Dealing the cards.")
    global deck
    global player_1_hand
    global player_2_hand
    player_1_hand = [random.choice(deck),
                     random.choice(deck),
                     random.choice(deck),
                     random.choice(deck),
                     random.choice(deck)]
    print(player_1_name + ", your starting hand is:")
    print(str(player_1_hand))
    player_2_hand = [random.choice(deck),
                     random.choice(deck),
                     random.choice(deck),
                     random.choice(deck),
                     random.choice(deck)]
    print(player_2_name + ", your starting hand is:")
    print(str(player_2_hand[0:]))
    return player_1_hand, player_2_hand, deck
    
def set_up_game():
    global deck
    global red_pile 
    global yellow_pile 
    global green_pile 
    global blue_pile 
    global discard_pile 

def introduce_players():
    global player_1_name
    global player_2_name
    global players
    player_1_name = input("Player 1, what is your name? ")
    player_2_name = input("Player 2, what is your name? ")
    players = [player_1_name, player_2_name]
    current_player = players[0]
    return player_1_name, player_2_name, players, current_player

def roll_dice():
    global players
    global current_player
    global die_roll
    global last_die_roll
    print(current_player, ", it's your turn.")
    if input("Press the spacebar + return to roll the dice.") == ' ':
        die_roll = int(random.randint(1,6))
        print (current_player + ", you rolled", die_roll)
        last_die_roll = die_roll
        return last_die_roll
    else:
        print("Sorry, I didn't get that. Press the spacebar + return to roll the dice.")
        roll_dice()
        
introduce_players()
build_deck()
print("Hello,", player_1_name, "and", player_2_name + "!")
print(player_1_name + ", you'll go first.")
print("Setting up the game.")
deal()
roll_dice()





