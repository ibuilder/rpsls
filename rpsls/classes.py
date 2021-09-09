class Characters():
    def __init__(self, weight, player, winphrase, losephrase):
        self.weight = weight
        self.player = player
        self.winphrase = winphrase
        self.losephrase = losephrase

    def __str__(self):
        return str(self.__dict__)


class User():
    def __init__(self, user):
        self.user = user

    def change_name(self, user):
        self.user = user
        return self.user


def battle(char_weight, npc_weight, char_player, npc_player, char_winphrase, npc_winphrase, char_losephrase, npc_losephrase, playerscore, npcscore):

    diff = (char_weight - npc_weight) % 5

    if diff == 0:
        print("It's a draw")
    elif diff >= 3:
        if char_weight > npc_weight:
            print(char_player, char_winphrase, npc_player)
            return char_player
        elif char_weight == npc_weight:
            print("It's a draw")
        else:
            print(npc_player, npc_winphrase, char_player)
            return npc_player

    elif diff <= 2:
        if char_weight < npc_weight:
            print(char_player, char_losephrase, npc_player)
            return char_player
        elif char_weight == npc_weight:
            print("It's a draw")
        else:
            print(npc_player, npc_losephrase, char_player)
            return npc_player
    else:
        print('Something went wrong')


def gameoptions():
    print("-----------------")
    print("1.  Rock")
    print("2.  Paper")
    print("3.  Lizard")
    print("4.  Spock")
    print("5.  Scissor")
    print("6.  Quit")
    print("-----------------")
