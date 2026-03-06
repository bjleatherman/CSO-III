from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict
from datetime import datetime
from Model.game_rules import GameRules
from Model.domain_models import *
from Model.enums import *
import uuid
import json

class OpponentAction(BaseModel):
    '''The public data that summarizes an opponents turn. Used to present to player'''

    # Opponent turn public info
    opp_direction: Optional[Direction] = None
    opp_power_used: Optional[Power] = None
    opp_weapon_target: Optional[Address] = None
    opp_new_surface: Optional[bool] = None
    opp_surface_sector: Optional[int] = None
    opp_is_surfaced: Optional[bool] = None
    opp_surface_duration_remaining: Optional[int] = None
    opp_received_damage: Optional[bool] = None
    opp_damage_source: Optional[DamageSource] = None
    opp_answer: Optional[SonarAnswer] = None

class TurnHeadline(BaseModel):
    '''The data that is shown to a player at the beginning of their turn. It should contain a summary of the public data that happened in the previous turn'''

    opponent_action: Optional[OpponentAction] = None

    # Info regarding player status/ required actions
    surface_duration_remaining: Optional[int] = None # Not sure if I need this
    damage_received: Optional[int] = None
    damage_source: Optional[DamageSource] = None
    drone_question_received: Optional[int] = None # Represents the id of the sector being scanned
    sonar_question_recieved: Optional[bool] = None

class Turn(BaseModel):
    '''All pieces of informatiopn that (may) need to be collected during a turn'''

    direction: Optional[Direction]
    sub_system_damaged: Optional[int]
    will_surface: Optional[bool]
    power_charged: Optional[Power]
    power_used: Optional[Power]
    mine_id_triggered: Optional[int]
    sonar_answer: Optional[SonarAnswer]