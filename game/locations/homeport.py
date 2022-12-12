
from game import location
import game.config as config
from game.display import announce
from game.player import Player
from game.ship import Ship

class HomePort (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "destination"
        self.symbol = 'H'

    def enter (self, ship):
        ship = config.the_player.ship
        if ship.get_treasure() < 5:
            announce("You cannot return to the home port until you collect five treasures.")
            
        else:
            config.the_player.gameInProgress = False
            announce ("congratulations you've reached home and won")
            Player.game_over()
