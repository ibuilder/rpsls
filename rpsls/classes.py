class Characters():
    def __init__(self, weight, player, winphrase, losephrase):
        self.weight = weight
        self.player = player
        self.winphrase = winphrase
        self.losephrase = losephrase

    def __str__(self):
        return str(self.__dict__)


class User():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def change_name(self, user):
        self.user = user
        return self.user

    def change_password(self, password):
        self.password = password
        return self.password


def battle(char_weight, npc_weight, char_player, npc_player, char_winphrase, npc_winphrase, char_losephrase, npc_losephrase, playerscore, npcscore):
    
    diff = (char_weight - npc_weight)%5
    
    if diff == 0:
        print ("It's a draw")
    elif diff >=3:
        if char_weight > npc_weight:
            playerscore = playerscore + 1
            print (char_player, char_winphrase, npc_player)
            print("You have", playerscore, "points and the computer has", npcscore, "points")
            return playerscore
        elif char_weight == npc_weight:
            print ("It's a draw")
            print("You have", playerscore, "points and the computer has", npcscore, "points")

        else:
            npcscore = npcscore + 1
            print (npc_player, npc_winphrase, char_player)
            print("You have", playerscore, "points and the computer has", npcscore, "points")
            return npcscore

    elif diff <=2:
        if char_weight < npc_weight:
            npcscore = npcscore + 1
            print (char_player, char_losephrase, npc_player)
            print("You have", playerscore, "points and the computer has", npcscore, "points")
            return npcscore
        elif char_weight == npc_weight:
            print ("It's a draw")
            print("You have", playerscore, "points and the computer has", npcscore, "points")
        else:
            playerscore = playerscore + 1
            print (npc_player, npc_losephrase, char_player)
            print("You have", playerscore, "points and the computer has", npcscore, "points")
            return playerscore

    else:
        print ('Something went wrong')

def gameoptions():
    print("-----------------")
    print("1.  Rock")
    print("2.  Paper")
    print("3.  Lizard")
    print("4.  Spock")
    print("5.  Scissor")
    print("6.  Quit")
    print("-----------------")