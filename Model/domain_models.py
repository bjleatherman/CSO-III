from pydantic import BaseModel, Field, model_validator
from typing import List, Optional, Tuple, Dict
from datetime import datetime
from Model.game_rules import GameRules
from enums import *
import uuid
import json

class Address(BaseModel):
    '''The data for an address. Contains row and col ints for easier reference in later in the game'''
    col_id: int
    row_id: int
    name: str # (i.e. A1)

    @model_validator(mode='before')
    @classmethod
    def set_address_name(cls, data):
        col = data.get('col_id')
        row = data.get('row_id')

        if col is not None and row is not None and not data.get('name'):
            data['name'] = cls.get_name(col, row)
        return data


    @staticmethod
    def get_name(col: int, row: int):
        '''Static utility: Converts (0, 0) -> 'A1', (26, 5) -> 'AA6'''
        
        col_name = ''
        col = col + 1
        
        while col > 0:
            col, remainder = divmod(col-1, 26)
            col_name = chr(65 + remainder) + col_name

        return f'{col_name}{row + 1}'
        

class Cell(BaseModel):
    '''The data that describes a cells composition'''
    is_water: bool
    is_land: bool
    address: Address
    sector: int

    @model_validator(mode='before')
    @classmethod
    def build_cell(cls, data):
        if 'is_water' in data and 'is_land' not in data:
            data['is_land'] = not data['is_water']
        
        if 'col' in data and 'row' in data:
            data['address'] = {
                'col_id': data.pop('col'),
                'row_id': data.pop('row')
            }
        return data

class Answer(BaseModel):
    '''Used as to relay infomation to the players'''
    drone_answer: Optional[bool] = None
    sonar_answer: Optional[Dict[MapIdLabels,int]] = None

class Mine(BaseModel):
    mine_id: int
    address: Address
    is_active: bool
    turn_detonated: int = None
