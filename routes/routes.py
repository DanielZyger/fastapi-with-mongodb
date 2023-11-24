from fastapi import APIRouter
from models.estudantes import Estudante
from models.curso import Curso
from config.estudante import estudantes_collection
from config.curso import curso_collection
from schema.estudante import list_serial_estudante
from schema.curso import list_serial_curso
from bson import ObjectId

router = APIRouter()

# GET Request
@router.get("/estudantes", tags=["estudantes"])
async def get_estudantes():
    estudantes = list_serial_estudante(estudantes_collection.find())
    return estudantes

# POST Request
@router.post("/estudantes", tags=["estudantes"])
async def post_estudante(estudante: Estudante):
    estudantes_collection.insert_one(dict(estudante))

# PUT Request
@router.put("/estudantes/{id}", tags=["estudantes"])
async def put_estudante(id: str, estudante: Estudante):
    estudantes_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(estudante)})

# DELETE Request
@router.delete("/estudantes/{id}", tags=["estudantes"])
async def delete_estudante(id: str):
    estudantes_collection.find_one_and_delete({"_id": ObjectId(id)})


# GET Request
@router.get("/cursos", tags=["cursos"])
async def get_cursos():
    cursos = list_serial_curso(curso_collection.find())
    return cursos

# POST Request
@router.post("/cursos", tags=["cursos"])
async def post_curso(curso: Curso):
    curso_collection.insert_one(dict(curso))

# PUT Request
@router.put("/cursos/{id}", tags=["cursos"])
async def put_curso(id: str, curso: Curso):
    curso_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(curso)})

# DELETE Request
@router.delete("/cursos/{id}", tags=["cursos"])
async def delete_curso(id: str):
    curso_collection.find_one_and_delete({"_id": ObjectId(id)})
