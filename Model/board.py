from Model.state import Cell
from typing import List, Optional, Tuple, Set
import random
from pydantic import BaseModel, Field, model_validator
from collections import deque

class Board(BaseModel):
    
    grid: List[List[Cell]]
    length: int
    width: int
    island_chance: float
    sector_width: int

    @classmethod
    def generate_board(cls, length, width, island_chance, sector_width) -> "Board":
        grid = []
        sectors_per_row = length // sector_width

        for y in range(width):
            row = []
            for x in range(length):
                r = random.random()
                is_water = r >= island_chance

                sector_x = x // sector_width
                sector_y = y // sector_width
                sector = sector_x + (sector_y * sectors_per_row) + 1

                cell = Cell(col=x, row=y, sector=sector, is_water=is_water)
                row.append(cell)
            grid.append(row)

        cls._ensure_connectivity(grid, length, width)

        return cls(
            grid=grid, length=length, width=width,
            island_chance=island_chance, sector_width=sector_width
        )

    @classmethod
    def _ensure_connectivity(cls, grid, length, width):
        # Find the first water cell
        start = None
        for y in range(width):
            for x in range(length):
                if grid[y][x].is_water:
                    start = (x, y)
                    break
            if start:
                break

        if not start:
            return

        # Flood fill from that one cell
        reachable = set()
        queue = deque([start])
        reachable.add(start)
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < length and 0 <= ny < width
                        and (nx, ny) not in reachable
                        and grid[ny][nx].is_water):
                    reachable.add((nx, ny))
                    queue.append((nx, ny))

        # Any water cell NOT reached becomes land
        for y in range(width):
            for x in range(length):
                if grid[y][x].is_water and (x, y) not in reachable:
                    grid[y][x].is_water = False
                    grid[y][x].is_land = True
    
    def get_cell(self, col_id: int, row_id: int) -> Optional[Cell]:
        '''Returns cell from grid at a given coordinate, reutrns None if coordinate is out-of-bounds'''
        
        if 0 <= col_id < self.length and 0 <= row_id < self.width:
            return self.grid[row_id][col_id] 
        return None # cell out-of-bounds
    
    def is_water(self, col_id: int, row_id: int) -> bool:
        cell = self.get_cell(col_id, row_id)
        return cell.is_water if cell else False
    
    def is_land(self, col_id: int, row_id: int) -> bool:
        cell = self.get_cell(col_id, row_id)
        return cell.is_land if cell else False
    
    #---------------#
    #---NEIGHBORS---#
    #---------------#

    #---Immediate Neighbors---#
    # Cardinal
    def get_cardinal_neighbors(self, col_id:int, row_id:int, only_water:bool=False) -> List[Cell]:
        return self.get_neighbors(col_id=col_id, row_id=row_id, only_water=only_water)
    
    
    # All Neighbors
    def get_all_neighbors(self, col_id:int, row_id:int, only_water:bool=False) -> List[Cell]:
        return self.get_neighbors(col_id=col_id, row_id=row_id, include_diagonals=True, only_water=only_water)
    
    #---Ranged Neighbors---#
    # Cardinal
    def get_cardinal_neighbors_in_range(self, col_id: int, row_id: int, grid_range: int, only_water: bool = False) -> List[Cell]:
        origin = self.get_cell(col_id=col_id, row_id=row_id)
        visited: Set[Cell] = {origin}
        frontier: Set[Cell] = {origin}

        for _ in range(grid_range):
            next_frontier: Set[Cell] = set()
            for cell in frontier:
                for neighbor in self.get_cardinal_neighbors(
                    col_id=cell.address.col_id,
                    row_id=cell.address.row_id,
                    only_water=only_water,
                ):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_frontier.add(neighbor)
            frontier = next_frontier

        return list(visited)
        
    # All Neighbors
    def get_all_neighbors_in_range(self, col_id: int, row_id: int, grid_range: int, only_water: bool = False) -> List[Cell]:
        origin = self.get_cell(col_id=col_id, row_id=row_id)
        visited: Set[Cell] = {origin}
        frontier: Set[Cell] = {origin}

        for _ in range(grid_range):
            next_frontier: Set[Cell] = set()
            for cell in frontier:
                for neighbor in self.get_all_neighbors(
                    col_id=cell.address.col_id,
                    row_id=cell.address.row_id,
                    only_water=only_water,
                ):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_frontier.add(neighbor)
            frontier = next_frontier

        return list(visited)

    # Calc
    def get_neighbors(self, col_id:int, row_id:int, include_diagonals:bool=False, only_water:bool=False):
        '''Returns existing neighboring cells around a coordinate'''
        if include_diagonals:
            offsets: List[Tuple[int, int]] = [
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1),
            ]
        else:
            offsets = [
                (0, -1),
                (1, 0),
                (0, 1),
                (-1, 0),
            ]
        neighbors: List[Cell] = []
        for col_shift, row_shift in offsets:
            cell = self.get_cell(col_id=col_id+col_shift, row_id=row_id+row_shift)
            
            # If cell exists and respects water flag, add it to the list
            if cell is not None and (not only_water or cell.is_water):
                neighbors.append(cell)

        return neighbors