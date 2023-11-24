from pydantic import BaseModel

class Curso(BaseModel):
    name: str
    description: str
    horas: int
    turno: str