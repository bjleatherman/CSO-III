from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict
from Model.domain_models import *
from Model.information import *
from enums import *
import uuid

class Charges(BaseModel):
    mine: int = 0
    torpedo: int = 0
    drone:int = 0
    sonar:int = 0
    silence:int = 0

class Submarine(BaseModel):
    # Player_id
    player_id: int

    # Sub Charges
    charges: Charges = Field(default_factory=Charges)

    # Player Data
    damage:int = 0
    systems_status: Dict[int, bool] = Field(default_factory=dict)
    mines_laid: List[Mine] = Field(default_factory=list)
    is_surfaced: bool = False
    surfaced_turn_count: int = 0
    location: Optional[Cell] = None

    @classmethod
    def create_default(cls, player_id: int):
        
        # Creates the systems id -> status dict to track systems status. 
        # TODO: Get rid of the magic numbers
        initial_system_status = {i: True for i in range(0, 25)}
        
        return cls(
            player_id=player_id,
            systems_status=initial_system_status
        )