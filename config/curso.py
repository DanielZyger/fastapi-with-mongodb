from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:teste123@cluster0.06rlw0d.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

curso_collection = db["cursos"]