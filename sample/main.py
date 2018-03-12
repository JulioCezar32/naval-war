from player import Player
from match import Match
from ships_models import *
from setupboard import SetUpBoard

player_one = Player('Joao')
player_two = Player('Maria')

board = SetUpBoard(4).get_board()

player_one.create_ship(Encouracado('2A'))
player_two.create_ship(Encouracado('2A'))

player_one.launch_bomb('1A')
player_two.launch_bomb('1A')

match = Match(player_one, player_two, board)
print(match.get_result())
