from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict
from datetime import datetime
from Model.game_rules import GameRules
from Model.domain_models import *
from Model.information import *
from Model.submarine import *
from enums import *
import uuid
import json

class GameState(BaseModel):
    '''Represents board on the current turn'''
    
    # Turn information
    turn_number: int = 0
    player_turn: int = 0

    # Board Info
    player_location: List[Tuple[Optional[int], Optional[int]]] = [(None, None), (None, None)]

    # Player Data
    subs: List[Submarine]


class GameHistory(BaseModel):
    '''the full save file containing an array of game states'''
    save_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = Field(default_factory=datetime.now)
    
    game_rules:GameRules
    grid: List[List[Cell]]
    history: List[GameState] = []
    
    direction_history: List[List[Direction]] = [[],[]]
    turn_history: List[Optional[Turn]] = []
    turn_headline_history: List[Optional[TurnHeadline]] = []

    @classmethod
    def create_initial_state(cls, game_rules:GameRules):

        from board import Board
        grid = Board.generate_grid(
            length=game_rules.length, 
            width=game_rules.width, 
            island_chance=game_rules.island_prob, 
            sector_width=game_rules.sector_width)

        initial_state = GameState()

        return cls(grid=grid, history=[initial_state], game_rules=game_rules)

    def get_current_game_state(self):
        return self.history[-1]