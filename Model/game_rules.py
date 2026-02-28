from pydantic import BaseModel, ConfigDict
from typing import List

class GameRules(BaseModel):
    '''The rule set for the game. Preset is standard rules'''

    model_config = ConfigDict(frozen=True)

    # Board
    length: int = 15
    width: int = 15
    sector_width: int = 5
    island_prob: float = 0.15
    sub_grid: int = 5

    # Player Charges
    max_mine_charge: int = 3
    max_torpedo_charge: int = 3
    max_drone_charge: int = 4
    max_sonar_charge: int = 3
    max_silence_charge: int = 6
    max_damage:int = 4

    # Power Effects
        # Mines
    mine_max_drop_range: int = 1
    mine_explosion_range: int = 2
    mine_indirect_damage: int = 1
    mine_direct_damage: int = 2
        # Torpedo
    torpedo_max_fire_range: int = 4
    torpedo_explosion_range: int = 2
    torpedo_indirect_damage: int = 1
    torpedo_direct_damage: int = 2
        # Silence
    silence_max_travel_range: int = 4

    # Other
    surface_turn_duration: int = 3