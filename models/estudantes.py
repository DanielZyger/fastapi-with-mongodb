from pydantic import BaseModel

class Estudante(BaseModel):
    name: str
    curso: str
    turno: str
