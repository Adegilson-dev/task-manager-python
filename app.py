class Tarefa:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.name} | Status: {self.status}"
        
    def to_dict(self):
        return {"id": self.id, "name": self.name, "status": self.status}


import json

tasksList = []
currentId = 0
