from player import Player
from match import Match
from ships_models import *
from setupboard import SetUpBoard
from pprint import *

player_one = Player('Joao')
player_two = Player('Maria')

#board = SetUpBoard(8).get_board()

    #ships names Encouracado, PortaAvioes, Destroyer, Submarino, BarcoDePatrulha
player_one.create_ship(Destroyer('1C'))
player_two.launch_bomb('4A')
print(player_one.ship.name)
match = Match(player_one, player_two, 4)
ships = match.plot_ship()

pprint(match.get_board())
print(match.get_result())
