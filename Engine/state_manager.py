from Model.state import GameState, GameHistory
from Model.game_rules import GameRules
from Model.api_models import *
from Model.domain_models import Address, Cell
from uuid import uuid4
from Engine.validators import ActionValidator

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
    
    def process_turn(self, turn: FullTurnRequest, player_id:int) -> GameHistory:

        candidate_state = self.history.create_next_state()
        previous_state = self.get_current_state()
        rules=self.history.game_rules

        candidate_turn_num = candidate_state.turn_number
        previous_turn_num = previous_state.turn_number

        # Check if requesting spawn
        if turn.spawn is not None:
            ActionValidator.validate_spawn(
                candidate_state=candidate_state,
                SpawnRequest=turn.spawn,
                board=self.history.board,
                player_id=player_id
                )