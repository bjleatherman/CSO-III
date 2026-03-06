import sys, math
from Model.state import GameHistory, GameState, Cell
from colorama import init, Back, Style

init(autoreset=True)

class Display:
    
    @staticmethod
    def draw_state(state:GameState, grid):
        
        # RGB Background Helpers
        # Format: \033[48;2;R;G;Bm
        def bg_rgb(r, g, b):
            return f"\033[48;2;{r};{g};{b}m"
            
        RESET = "\033[0m"
        
        # Define specific RGB colors
        # Ocean: Deep Blue (0, 105, 148)
        OCEAN_COLOR = bg_rgb(0, 105, 148)
        # Land: Bright Green (34, 139, 34)
        LAND_COLOR = bg_rgb(34, 139, 34)

        # @staticmethod
        def print_grid_to_console(state, grid):

            # Print Column labels
            row_count = len(grid)
            max_label_w = len(str(row_count))
            
            print(f'{" ":<{max_label_w}} ', end="") 
            for c, _ in enumerate(grid[0]):
                print(f"{chr(c + 65)} ", end="")
            print()

            # Print Grid
            for y, row in enumerate(grid):
                print(f'{y+1:>{max_label_w}} ', end="")

                for x, cell in enumerate(row):
                    if cell.is_water:
                        content = f'{OCEAN_COLOR}  {RESET}'
                    if cell.is_land:
                        content = f'{LAND_COLOR}  {RESET}'
                    print(content, end="")
                print()
        
        sys.stdout.reconfigure(encoding='utf-8')
        print_grid_to_console(state, grid)
        sys.stdout.flush()