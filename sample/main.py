from player import Player
from match import Match



player_one = Player('Joao')
player_two = Player('Maria')

player_one.create_ship(Encouracado(),'A2')
player_two.create_ship(Encouracado(),'A2')

player_one.launch_bomb('A2')
player_two.launch_bomb('A2')

match = Match(player_one, player_two)
print(match.get_result())
