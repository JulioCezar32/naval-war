from player import Player
from match import Match
from ships_models import *
from setupboard import SetUpBoard
from pprint import *

player_one = Player('Joao')
player_two = Player('Maria')

#board = SetUpBoard(8).get_board()

    #ships names Encouracado, PortaAvioes, Destroyer, Submarino, BarcoDePatrulha
player_one.create_ship(Encouracado('2A'))
player_two.launch_bomb('2A')

match = Match(player_one, player_two, 5)
ships = match.plot_ship()

pprint(match.get_board())
print(match.get_result())
