from pydantic import BaseModel
from Model.enums import *
from Model.state import *
from Model.game_rules import *
from Model.information import *
from Model.submarine import *
from Model.domain_models import *

class SpawnRequest(BaseModel):
    player_id: int
    col_id: int
    row_id: int

class DirectionRequest(BaseModel):
    direction: Direction

class SurfaceRequest(BaseModel):
    surface: bool = True

class MaintainSurfaceRequest(BaseModel):
    surface: bool = True

class EndSurfaceRequest(BaseModel):
    end_surface: bool = True

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

class FullTurnRequest(BaseModel):
    player_id: int
    is_surfacing: bool = False
    
    movement_phase: Optional[Direction] = None
    charge_phase: Optional[ChargePowerRequest] = None
    subsystem_phase: Optional[SubSystemRequest] = None
    power_phase: Optional[UsePowerRequest] = None
    mine_detonation_phase: Optional[DetonateMineRequest] = None
    sonar_answer_phase: Optional[SonarAnswerRequest] = None