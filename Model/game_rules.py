from pydantic import BaseModel, ConfigDict
from typing import List
from Model.domain_models import *

class GameRules(BaseModel):
    '''The rule set for the game. Preset is standard rules'''

    model_config = ConfigDict(frozen=True)

    # Board
    length: int = 15
    width: int = 15
    sector_width: int = 5
    island_prob: float = 0.15
    sub_grid: int = 5

    # Player Rules
    number_of_players: int = 2

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

    # SubSystem Layout
    subsystem_layout: List[SubSystemBlueprint] = Field(default_factory=lambda: [
        # --- WEST COLUMN ---
            SubSystemBlueprint(system_id=1, direction_group=Direction.WEST, power_group=PowerGroup.WEAPONS, pipe_group=PipeGroup.YELLOW),
            SubSystemBlueprint(system_id=2, direction_group=Direction.WEST, power_group=PowerGroup.STEALTH, pipe_group=PipeGroup.YELLOW),
            SubSystemBlueprint(system_id=3, direction_group=Direction.WEST, power_group=PowerGroup.RECON, pipe_group=PipeGroup.YELLOW),
            SubSystemBlueprint(system_id=4, direction_group=Direction.WEST, power_group=PowerGroup.RECON, pipe_group=None),
            SubSystemBlueprint(system_id=5, direction_group=Direction.WEST, power_group=PowerGroup.REACTOR, pipe_group=None),
            SubSystemBlueprint(system_id=6, direction_group=Direction.WEST, power_group=PowerGroup.REACTOR, pipe_group=None),

            # --- NORTH COLUMN ---
            SubSystemBlueprint(system_id=7, direction_group=Direction.NORTH, power_group=PowerGroup.STEALTH, pipe_group=PipeGroup.ORANGE),
            SubSystemBlueprint(system_id=8, direction_group=Direction.NORTH, power_group=PowerGroup.WEAPONS, pipe_group=PipeGroup.ORANGE),
            SubSystemBlueprint(system_id=9, direction_group=Direction.NORTH, power_group=PowerGroup.STEALTH, pipe_group=PipeGroup.ORANGE),
            SubSystemBlueprint(system_id=10, direction_group=Direction.NORTH, power_group=PowerGroup.RECON, pipe_group=None),
            SubSystemBlueprint(system_id=11, direction_group=Direction.NORTH, power_group=PowerGroup.WEAPONS, pipe_group=None),
            SubSystemBlueprint(system_id=12, direction_group=Direction.NORTH, power_group=PowerGroup.REACTOR, pipe_group=None),

            # --- SOUTH COLUMN ---
            SubSystemBlueprint(system_id=13, direction_group=Direction.SOUTH, power_group=PowerGroup.RECON, pipe_group=PipeGroup.GREY),
            SubSystemBlueprint(system_id=14, direction_group=Direction.SOUTH, power_group=PowerGroup.STEALTH, pipe_group=PipeGroup.GREY),
            SubSystemBlueprint(system_id=15, direction_group=Direction.SOUTH, power_group=PowerGroup.WEAPONS, pipe_group=PipeGroup.GREY),
            SubSystemBlueprint(system_id=16, direction_group=Direction.SOUTH, power_group=PowerGroup.WEAPONS, pipe_group=None),
            SubSystemBlueprint(system_id=17, direction_group=Direction.SOUTH, power_group=PowerGroup.REACTOR, pipe_group=None),
            SubSystemBlueprint(system_id=18, direction_group=Direction.SOUTH, power_group=PowerGroup.STEALTH, pipe_group=None),

            # --- EAST COLUMN ---
            SubSystemBlueprint(system_id=19, direction_group=Direction.EAST, power_group=PowerGroup.RECON, pipe_group=PipeGroup.ORANGE),
            SubSystemBlueprint(system_id=20, direction_group=Direction.EAST, power_group=PowerGroup.STEALTH, pipe_group=PipeGroup.GREY),
            SubSystemBlueprint(system_id=21, direction_group=Direction.EAST, power_group=PowerGroup.WEAPONS, pipe_group=PipeGroup.YELLOW),
            SubSystemBlueprint(system_id=22, direction_group=Direction.EAST, power_group=PowerGroup.REACTOR, pipe_group=None),
            SubSystemBlueprint(system_id=23, direction_group=Direction.EAST, power_group=PowerGroup.RECON, pipe_group=None),
            SubSystemBlueprint(system_id=24, direction_group=Direction.EAST, power_group=PowerGroup.REACTOR, pipe_group=None),
    ])