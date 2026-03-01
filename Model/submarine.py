from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict
from Model.domain_models import *
from Model.information import *
from Model.enums import *
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
    mines_laid: Dict[int, Mine] = Field(default_factory=dict)
    is_surfaced: bool = False
    surfaced_turn_count: int = 0
    location: Optional[Address] = None
    location_history: Optional[Dict[int, Address]] = None

    @classmethod
    def create_default(cls, player_id: int):
        
        # Creates the systems id -> status dict to track systems status. 
        # TODO: Get rid of the magic numbers
        initial_system_status = {i: True for i in range(0, 24)}
        
        return cls(
            player_id=player_id,
            systems_status=initial_system_status
        )
    
    #--------------#
    #---LOCATION---#
    #--------------#

    def set_location(self, address:Address, turn_number:int):
        self.location = address
        self.location_history[turn_number] = address

    def spawn_at(self, col_id:int, row_id:int, turn_number:int):
        address = Address(col_id=col_id, row_id=row_id)
        self.set_location(address, turn_number=turn_number)

    def start_surface(self, turn_number:int):
        self.is_surfaced = True
        self.surfaced_turn_count = 1
        self.set_location(self.location, turn_number=turn_number)

    def increment_surface(self, turn_number:int):
        self.surfaced_turn_count += 1
        self.set_location(self.set_location, turn_number=turn_number)

    def end_surface(self, turn_number:int):
        self.is_surfaced = False
        self.surfaced_turn_count = 0
        self.repair_all_systems()

        # TODO: Do I need to have the move action inside  of the end_surface funciton?
            # I feel like this should be handled by the validator?


    #------------#
    #---DAMAGE---#
    #------------#

    def take_damage(self, damage_amount:int):
        '''Return True if Sub is Still Alive, False if Sub Sank'''
        self.damage -= self.damage_amount
        return self.damage > 0
    
    
    #-------------#
    #---SYSTEMS---#
    #-------------#

    def damage_system_by_id(self, system_id:int):
        self.systems_status[system_id] = False

    def repair_system_by_id(self, system_id:int):
        self.systems_status[system_id] = True

    def batch_repair_system_by_id(self, system_ids:List[int]):
        for system_id in system_ids:
            self.repair_system_by_id(system_id=system_id)

    def repair_all_systems(self):
        for system_id, repair_status in self.systems_status:
            self.systems_status[system_id] = True

    #-------------#
    #---CHARGES---#
    #-------------#

    # Mines
    def charge_mine(self):
        self.charges.mine += 1

    def drop_mine(self, col_id:int, row_id:int, turn_number:int):
        # Spend the mine charge
        self.charges.mine = 0

        # TODO: Validate that the mine is being laid next to the sub and not in the path, if that should be done within this scope....
            # I think it should be in the validator scope of responsibilities
        # Get the next id for the mine
        if not self.mines_laid:
            next_id = 1
        else:
            next_id = max(self.mines_laid.keys()) + 1

        address = Address(col_id=col_id, row_id=row_id)
        mine = Mine(address=address, turn_created=turn_number)

        self.mines_laid[next_id] = mine

    def detonate_mine(self, mine_id:int, turn_number:int):
        if mine_id not in self.mines_laid:
            raise ValueError(f'Mine Id, {mine_id} does not exist')
        
        mine = self.mines_laid[mine_id]
        
        try:
            mine.detonate(turn_number=turn_number)
        except ValueError as e:
            raise ValueError(f'Failed to detonate mine {mine_id}: {e}') from e

    # Torpedos
    def charge_torpedo(self):
        self.charges.torpedo += 1

    def use_torpedo(self):
        self.charges.torpedo = 0

    # Drones
    def charge_drone(self):
        self.charges.drone += 1
    
    def use_drone(self):
        self.charges.drone = 0


    # Sonar
    def charge_sonar(self):
        self.charges.sonar += 1

    def use_sonar(self):
        self.charges.sonar = 0

    # Silence
    def charge_silence(self):
        self.charges.silence += 1

    def use_silence(self):
        self.charges.silence = 0