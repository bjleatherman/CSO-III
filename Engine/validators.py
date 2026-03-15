from Model.state import *
from Model.api_models import *
from Model.game_rules import *

class ActionValidator:

    @staticmethod
    def validate_spawn(candidate_state:GameState, spawn_request: SpawnRequest, board:Board, player_id:int) -> None:
        """Validates board boundaries and terrain constraints for initial deployment."""
        
        msg = 'Spawn Request Invlaid |'
        spawn_cell=board.get_cell(
            col_id=spawn_request.col_id, 
            row_id=spawn_request.row_id
            )

        if candidate_state.subs[player_id].location.name is not None:
            raise ValueError(f'{msg} Player {player_id} already exists at {candidate_state.subs[player_id].location.name}')

        # Must be in bounds
        if spawn_cell is None:
            raise ValueError(f'{msg} {spawn_request} : No such cell exists')

        if not spawn_cell.is_water:
            raise ValueError(f'{msg} {spawn_request} : Cell is not water')
       

    # @staticmethod
    # def validate_movement_phase(candidate_state: GameState, history: GameHistory, player_id: int, direction: Direction) -> None:
    #     """Evaluates boundary, terrain, and path history constraints for a standard movement."""
    #     # TODO: Implement grid math and intersection checks
    #     pass

    # @staticmethod
    # def validate_surfacing_phase(candidate_state: GameState, player_id: int) -> None:
    #     """Ensures the submarine is eligible to surface."""
    #     pass

    # @staticmethod
    # def validate_engineering_phase(candidate_state: GameState, player_id: int, charge: Power, system_id: int) -> None:
    #     """Verifies that the selected system damage is valid for the chosen direction and power charge."""
    #     # TODO: Check GameRules.subsystem_layout
    #     pass

    # @staticmethod
    # def validate_silence_movement(candidate_state: GameState, history: GameHistory, player_id: int, distance: int) -> None:
    #     """
    #     Validates the sequential steps of a Silence activation.
    #     Must evaluate the path constraint iteratively for the given distance.
    #     """
    #     if not (0 <= distance <= 4):
    #         raise ValueError("Silence distance must be between 0 and 4.")
    #     # TODO: Step-by-step path validation
    #     pass

    # @staticmethod
    # def validate_weapon_usage(candidate_state: GameState, player_id: int, request: TurnRequest) -> None:
    #     """Verifies charge levels, target ranges, and line-of-sight based on the candidate state's current location."""
    #     # TODO: Calculate range for torpedoes/mines
    #     pass