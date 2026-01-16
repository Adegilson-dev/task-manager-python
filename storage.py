import json
from models import Tarefa

def saveTasks(tasksList):
    with open("tarefas.json", "w") as f:
        json.dump([t.to_dict() for t in tasksList], f, indent=4)
    print("💾 Tarefas salvas em tarefas.json\n")


def loadTasks():
    try:
        with open("tarefas.json", "r") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Arquivo vazio ou corrompido. Começando do zero.\n")
                return [], 0

            tasksList = [Tarefa(t["id"], t["name"], t["status"]) for t in dados]
            currentId = max((t.id for t in tasksList), default=0)

        print("📂 Tarefas carregadas com sucesso!\n")
        return tasksList, currentId

    except FileNotFoundError:
        print("⚠️ Nenhum arquivo encontrado, começando do zero.\n")
        return [], 0
