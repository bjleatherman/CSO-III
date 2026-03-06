from Model.state import GameState, GameHistory
from Model.game_rules import GameRules
from Model.api_models import *
from Model.domain_models import Address, Cell
from uuid import uuid4

class StateManager:

    history:GameHistory

    def __init__(self, history:GameHistory=None):
        if history == None:
            game_rules = GameRules()
            self.history = GameHistory.create_initial_state(game_rules)
        else:
            self.history = history

    def get_current_state(self):
        return self.history.get_current_game_state()
    
    def process_turn(self, request: FullTurnRequest) -> GameHistory:

        candidate_state = self.history.create_next_state()