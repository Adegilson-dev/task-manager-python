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


def saveTasks():
    with open("tarefas.json", "w") as f:
        json.dump([t.to_dict() for t in tasksList], f, indent=4)
    print("💾 Tarefas salvas em tarefas.json\n")
