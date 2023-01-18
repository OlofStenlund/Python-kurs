from typing import List
from enum import Enum

class Player(Enum):
    Player1 = "X"
    Player2 = "O"

class Game:
    
    def __init__(self, player):
        self.player = Player

