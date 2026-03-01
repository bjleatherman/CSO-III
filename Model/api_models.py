from pydantic import BaseModel

class SpawnRequest(BaseModel):
    player_id: int
    col_id: int
    row_id: int