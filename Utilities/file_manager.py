import os
from pathlib import Path
from dotenv import load_dotenv
from Model.state import GameHistory

class FileManager:
        
    load_dotenv()

    @staticmethod
    def _get_full_path(file_uuid: str) -> Path:
        save_dir = Path(os.getenv('SAVE_DIR', "files/save_files"))
        save_dir.mkdir(parents=True, exist_ok=True)
        return save_dir / f"{file_uuid}.json"

    @staticmethod
    def save(history: GameHistory) -> None:
        """Serializes a GameHistory object and commits it to disk."""
        path = FileManager._get_full_path(history.save_id)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(history.model_dump_json(indent=2))

    @staticmethod
    def load(file_uuid: str) -> GameHistory:
        """Reads JSON from disk and returns a hydrated GameHistory object."""
        path = FileManager._get_full_path(file_uuid)
        if not path.exists():
            raise FileNotFoundError(f"Save file {file_uuid} not found.")
        
        with open(path, 'r', encoding='utf-8') as f:
            return GameHistory.model_validate_json(f.read())