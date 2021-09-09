import random

from rpsls.classes import Characters, User, battle, gameoptions

playerscore = 0
npcscore = 0

choice1 = Characters(1, "Rock", "crushes","crushes")
choice2 = Characters(2, "Paper", "covers","disproves")
choice3 = Characters(3, "Lizard", "eats","poisons")
choice4 = Characters(4, "Spock", "vaporizes", "smashes")
choice5 = Characters(5, "Scissor", "cuts","decpitates")

choices = [choice1, choice2, choice3, choice4, choice5]

playeruser = input("What is your username? ")
playerpass = input("What is your password? ")
player = User(playeruser, playerpass)

print("Welcome", player.user, "!")

#NPC Character variables
npc_choice = vars(random.choice(choices))
print(npc_choice)
npc_weight = npc_choice['weight']
npc_player = npc_choice['player']
npc_winphrase = npc_choice['winphrase']
npc_losephrase = npc_choice['losephrase']

#Player character variables

character = "0"
while character != "6":
    gameoptions()
    character = input("Pick a  number? ")
    if character == "1":
        character = vars(choice1)
    elif  character == "2":
        character = vars(choice2)
    elif  character == "3":
        character = vars(choice3)
    elif  character == "4":
        character = vars(choice4)
    elif  character == "5":
        character = vars(choice5)
    else:
        break

    char_weight = character['weight']
    char_player = character['player']
    char_winphrase = character['winphrase']
    char_losephrase = character['losephrase']


    print("You Picked: " + char_player)


    print("Opposed by.. " + npc_player)


    battle(char_weight, npc_weight, char_player, npc_player, char_winphrase, npc_winphrase, char_losephrase, npc_losephrase, playerscore, npcscore)

print("Game Over\n")
print("===Final Score====")
print("Player Score:", playerscore, "points | Computer Score:", npcscore, "points")