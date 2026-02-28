from enum import Enum, StrEnum, IntEnum

class Direction(StrEnum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

class PipeGroup(StrEnum):
    YELLOW = 'yellow_pipe'
    ORANGE = 'orange_pipe'
    GREY = 'grey_pipe'

class PowerGroup(StrEnum):
    WEAPONS = 'weapons_group'
    RECON = 'recon_group'
    STEALTH = 'stealth_group'
    REACTOR = 'reactor_group' # Used for SubSystems

class Power(StrEnum):
    MINE = 'mine'
    TORPEDO = 'torpedo'
    DRONE = 'drone'
    SONAR = 'sonar'
    SILENCE = 'silence'

class MapIdLabels(StrEnum):
    ROW_ID = 'row_id'
    COL_ID = 'col_id'
    SECTOR_ID = 'sector_id'

class Question(StrEnum):
    DRONE_QUESTION = 'drone_question'
    SONAR_QUESTION = 'sonar_question'

class DamageSource(StrEnum):
    TERRAIN = 'terrain'
    REACTOR = 'reactor'
    MINE = 'mine'
    TORPEDO = 'torpedo'
    