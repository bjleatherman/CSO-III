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
    
    def spawn_player(self, request: SpawnRequest):
        current_state = self.get_current_state()
        rules = self.history.game_rules

        request_address = Address.get_name(request.col_id, request.row_id)

        # Validate
        if not (0<= request.col_id < rules.width) or not (0 <= request.row_id < rules.length):
            raise ValueError(f'Spawn Coordinates: ({request_address}) Out of Bounds')
        
        target_cell = self.history.grid[request.row_id][request.col_id]
        if target_cell.is_land:
            raise ValueError(f'Spawn Coordinates: ({request_address}) Cannot be on Land')
        
        sub = current_state.subs[request.player_id]
        if sub.location is not None:
            raise ValueError('Player has already spawned')
        
        # Mutate
        next_state = current_state.model_copy(deep=True)
        next_sub = next_state.subs[request.player_id]

        next_sub.location = (request.col_id, request.row_id)

        self.history.history.append(next_state)

        return self.history