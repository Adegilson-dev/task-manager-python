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

def loadTasks():
    global tasksList, currentId
    try:
        with open("tarefas.json", "r") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Arquivo vazio ou corrompido. Começando do zero.\n")
                return
            tasksList = [Tarefa(t["id"], t["name"], t["status"]) for t in dados]
            if tasksList:
                currentId = max(t.id for t in tasksList)
        print("📂 Tarefas carregadas com sucesso!\n")
    except FileNotFoundError:
        print("⚠️ Nenhum arquivo encontrado, começando do zero.\n")


def addTask():
    global currentId
    name = input("Insira o nome da tarefa: ")
    status = False
    currentId += 1
    tarefa = Tarefa(currentId, name, status)
    tasksList.append(tarefa)
    print("✅ Tarefa adicionada com sucesso!\n")
    saveTasks()

def listTasks():
    if not tasksList:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        print("=== Lista de Tarefas ===")
        print(f"{'ID':<3} {'Nome':<20} {'Status':<5}")
        print("-" * 30)
        for task in tasksList:
            if task.status == True:
                print(f"{task.id:<3} {task.name:<20} [✓]\n")
            else:
                print(f"{task.id:<3} {task.name:<20} [ ]\n")

def removeTask():
    if not tasksList:
        print("Nenhuma tarefa cadastrada.\n")
        return

    selectId = int(input("Selecione o ID da tarefa que deseja remover: "))
    for task in tasksList:
        if selectId == task.id:
            confirm = input(
                f"Tem certeza que quer remover {task.name}? Essa ação é irreversível. (Y/N): "
            ).upper()
            if confirm == "Y":
                tasksList.remove(task)
                print("❌ Tarefa removida com sucesso!\n")
                saveTasks()
            else:
                print("Operação cancelada.\n")
            return

def completeTask():
    if not tasksList:
        print("Nenhuma tarefa cadastrada.\n")
        return

    selectId = int(input("Selecione o ID da tarefa que deseja completar: "))
    for task in tasksList:
        if selectId == task.id:
            task.status = True
            print("✅ Tarefa completada com sucesso!\n")
            saveTasks()
            return
