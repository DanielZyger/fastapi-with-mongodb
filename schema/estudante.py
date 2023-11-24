def individual_serial(estudante) ->  dict:
    return {
        "id": str(estudante["_id"]),
        "name": estudante["name"],
        "curso": estudante["curso"],
        "turno": estudante["turno"],
    }
    
def list_serial_estudante(estudantes) -> list:
    return [individual_serial(estudante) for estudante in estudantes]
    