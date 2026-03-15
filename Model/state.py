from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict
from datetime import datetime
from Model.game_rules import GameRules
from Model.domain_models import *
from Model.information import *
from Model.submarine import *
from Model.enums import *
from Model.board import *
import uuid
import json

class GameState(BaseModel):
    '''Represents board on the current turn'''
    
    # Turn information
    turn_number: int = 0
    player_turn: int = 0

    # Player Data
    subs: Dict[int, Submarine]

    def create_next_state(self, turn_number:int, player_turn:int) -> 'GameState':
        '''Creates a deep copy of the turn state and advances the turn clock'''
        next_state = self.model_copy(deep=True)

        next_state.turn_number = turn_number
        next_state.player_turn = player_turn

        return next_state


class GameHistory(BaseModel):
    '''the full save file containing an array of game states'''
    save_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = Field(default_factory=datetime.now)

    turn_number: int = 0 
    player_turn: int = 0
    
    game_rules:GameRules
    board: Board
    history: Dict[int, GameState]

    direction_history: List[Dict[int, Direction]] = Field(default_factory=list)
    turn_history: List[Dict[int, Turn]] = Field(default_factory=list)
    turn_headline_history: List[Dict[int, TurnHeadline]] = Field(default_factory=list)


    @classmethod
    def create_initial_state(cls, game_rules:GameRules):
        ''' Creates the board, GameHistory data structures, and the starting state of the game'''
        
        player_count = game_rules.number_of_players

        # Generate a new board using the game rules
        board = Board.generate_board(
            length=game_rules.length, 
            width=game_rules.width, 
            island_chance=game_rules.island_prob, 
            sector_width=game_rules.sector_width)

        # Create subs for each player
        subs = {x: Submarine.create_default(player_id=x) for x in range(player_count)}
        initial_state = {0: GameState(subs=subs)}

        
        init_direction_history = [{} for _ in range(player_count)]
        init_turn_history = [{} for _ in range(player_count)]
        init_turn_headline_history = [{} for _ in range(player_count)]

        return cls(board=board, 
                   history=initial_state, 
                   game_rules=game_rules,
                   direction_history=init_direction_history,
                   turn_history=init_turn_history,
                   turn_headline_history=init_turn_headline_history
                   )

    def get_current_game_state(self):
        return self.history[self.turn_number]
    
    def create_next_state(self):
        previous_state = self.get_current_game_state()

        next_turn_number = self.turn_number + 1
        next_player_turn = self.get_next_player_number()

        next_state = previous_state.create_next_state(turn_number=next_turn_number, player_turn=next_player_turn)

        return next_state
    
    def commit_turn(self, next_state:GameState, 
                    player_id:int, 
                    direction:Optional[Direction], 
                    turn: Optional[Turn], 
                    turn_headline:Optional[TurnHeadline]):
        
        self.history[next_state.turn_number] = next_state
        self.turn_number = next_state.turn_number
        self.player_turn = next_state.player_turn

        if direction:
            self.direction_history[player_id][next_state.turn_number] = direction

        if turn:
            self.turn_history[player_id][next_state.turn_number] = turn

        if turn_headline:
            self.turn_headline_history[player_id][next_state.turn_number] = turn_headline

    def get_next_player_number(self):
        
        if self.player_turn + 1 < self.game_rules.number_of_players:
            return self.player_turn + 1
        else:
            return 0