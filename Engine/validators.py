from Model.state import *
from Model.api_models import *

class ActionValidator:

    @staticmethod
    def validate_spawn(history: GameHistory, request: SpawnRequest) -> None:
        """Validates board boundaries and terrain constraints for initial deployment."""
        pass # Implementation from previous steps

    @staticmethod
    def validate_movement_phase(candidate_state: GameState, history: GameHistory, player_id: int, direction: Direction) -> None:
        """Evaluates boundary, terrain, and path history constraints for a standard movement."""
        # TODO: Implement grid math and intersection checks
        pass

    @staticmethod
    def validate_surfacing_phase(candidate_state: GameState, player_id: int) -> None:
        """Ensures the submarine is eligible to surface."""
        pass

    @staticmethod
    def validate_engineering_phase(candidate_state: GameState, player_id: int, charge: Power, system_id: int) -> None:
        """Verifies that the selected system damage is valid for the chosen direction and power charge."""
        # TODO: Check GameRules.subsystem_layout
        pass

    @staticmethod
    def validate_silence_movement(candidate_state: GameState, history: GameHistory, player_id: int, distance: int) -> None:
        """
        Validates the sequential steps of a Silence activation.
        Must evaluate the path constraint iteratively for the given distance.
        """
        if not (0 <= distance <= 4):
            raise ValueError("Silence distance must be between 0 and 4.")
        # TODO: Step-by-step path validation
        pass

    @staticmethod
    def validate_weapon_usage(candidate_state: GameState, player_id: int, request: TurnRequest) -> None:
        """Verifies charge levels, target ranges, and line-of-sight based on the candidate state's current location."""
        # TODO: Calculate range for torpedoes/mines
        pass