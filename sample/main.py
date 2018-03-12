from player import Player
from match import Match
from ships_models import *
from setupboard import SetUpBoard
from pprint import *

player_one = Player('Joao')
player_two = Player('Maria')

board = SetUpBoard(4).get_board()
player_one.create_ship(Encouracado('1A'))
player_two.launch_bomb('2A')

match = Match(player_one, player_two, board)
pprint(board)
print(match.get_result())
