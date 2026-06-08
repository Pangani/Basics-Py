print('Lambdas Exercise')

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

#Sort this by score using lambda!
player_list.sort(key=lambda player: player.score)
print([player.name for player in player_list])