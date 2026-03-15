from pydantic import BaseModel
from Model.enums import *
from Model.state import *
from Model.game_rules import *
from Model.information import *
from Model.submarine import *
from Model.domain_models import *

class SpawnRequest(BaseModel):
    col_id: int
    row_id: int

class DirectionRequest(BaseModel):
    direction: Direction

class SurfaceRequest(BaseModel):
    surface: bool = True

class ChargePowerRequest(BaseModel):
    power: Power

class DamageSubmarineRequest(BaseModel):
    damage_amount: int

class SubSystemRequest(BaseModel):
    subsystem_id: int

class UsePowerRequest(BaseModel):
    power: Power
    col_id: Optional[int] = None
    row_id: Optional[int] = None
    sector_id: Optional[int] = None
    silence_directions: Optional[List[Direction]] = Field(default_factory=list)

class DetonateMineRequest(BaseModel):
    mine_id: int

class SonarAnswerRequest(BaseModel):
    sonar_answer: Tuple[MapIdLabels, SonarAnswerData] = Field(default_factory=tuple)

    # @model_validator(mode='before')
    # @classmethod
    # def set_sonar_answer_request(cls, ):

class DroneAnswerRequest(BaseModel):
    drone_answer: Optional[bool] = None

class FullTurnRequest(BaseModel):
    
    # Player
    player_id: int

    # Spawn Request
    spawn: Optional[SpawnRequest] = None

    # Surface
    is_surfacing: bool = False
    
    # Pending Questions Answered
    sonar_answer_phase: Optional[SonarAnswerRequest] = None
    drone_answer_phase: Optional[DroneAnswerRequest] = None
    
    # Normal Turn
    movement_phase: Optional[Direction] = None
    charge_phase: Optional[ChargePowerRequest] = None 
    subsystem_phase: Optional[SubSystemRequest] = None
    power_phase: Optional[UsePowerRequest] = None
    mine_detonation_phase: Optional[DetonateMineRequest] = None