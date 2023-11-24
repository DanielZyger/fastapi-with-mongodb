def individual_serial(estudante) ->  dict:
    return {
        "id": str(estudante["_id"]),
        "name": estudante["name"],
        "description": estudante["description"],
        "horas": estudante["horas"],
        "turno": estudante["turno"]
    }
    
def list_serial_curso(estudantes) -> list:
    return [individual_serial(estudante) for estudante in estudantes]
