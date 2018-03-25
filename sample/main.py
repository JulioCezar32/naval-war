from player import Player
from match import Match
from ships_models import *
from pprint import *

player_one = Player('Joao')
player_two = Player('Maria')

#board = SetUpBoard(8).get_board()

    #ships names Encouracado, PortaAvioes, Destroyer, Submarino, BarcoDePatrulha
player_one.create_ship(Destroyer('1A'))
player_one.create_ship(PortaAvioes('1C'))
player_one.create_ship(Destroyer('3C'))
player_one.create_ship(Destroyer('2E'))
player_one.create_ship(Destroyer('1D'))
player_two.launch_bomb('3A')
player_two.launch_bomb('1A')
player_two.launch_bomb('3D')
player_two.launch_bomb('2A')
player_two.launch_bomb('3D')
player_two.launch_bomb('2E')
match = Match(player_one, player_two, 5)
print(match.bombs_positions)

print(match.get_result())
print(match.destroyed_ship())
pprint(match.board)
