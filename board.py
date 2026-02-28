from Model.state import GameState, Cell
from typing import List, Optional
import random

class Board:
    # grid = []

    # def __init__(self, grid:GameState.grid=None):
        
    #     if grid == None:
    #         self.grid = self.generate_grid()
    #     else:
            # self.grid = grid

    @staticmethod
    def generate_grid(length=15, width=15, island_chance=0.15, sector_width=5):
        
        grid = []
        sectors_per_row = width // sector_width

        for y in range(length):
            row = []
            for x in range(width):
                r = random.random()
                is_water = r >= island_chance
                
                sector_x = x // sector_width
                sector_y = y // sector_width
                sector = sector_x + (sector_y * sectors_per_row) + 1

                cell = Cell(col=x, 
                            row=y, 
                            sector=sector,
                            is_water=is_water)
                row.append(cell)
            grid.append(row)
        return grid