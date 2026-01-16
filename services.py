from models import Tarefa
from storage import saveTasks


def addTask(tasksList, currentId):
    name = input("Insira o nome da tarefa: ").strip()
    if not name:
        print("❌ Nome da tarefa não pode ser vazio.\n")
        return currentId

    currentId += 1
    tarefa = Tarefa(currentId, name, False)
    tasksList.append(tarefa)

    print("✅ Tarefa adicionada com sucesso!\n")
    saveTasks(tasksList)
    return currentId


def listTasks(tasksList):
    if not tasksList:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("=== Lista de Tarefas ===")
    print(f"{'ID':<3} {'Nome':<50} {'Status'}")
    print("-" * 70)

    for task in tasksList:
        status = "[✓]" if task.status else "[ ]"
        print(f"{task.id:<3} {task.name:<50} {status}")


def removeTask(tasksList):
    if not tasksList:
        print("Nenhuma tarefa cadastrada.\n")
        return

    try:
        selectId = int(input("Selecione o ID da tarefa: "))
    except ValueError:
        print("❌ ID inválido.\n")
        return

    for task in tasksList:
        if task.id == selectId:
            confirm = input(f"Remover '{task.name}'? (Y/N): ").upper()
            if confirm == "Y":
                tasksList.remove(task)
                saveTasks(tasksList)
                print("❌ Tarefa removida.\n")
            else:
                print("Operação cancelada.\n")
            return

    print("⚠️ Tarefa não encontrada.\n")


def completeTask(tasksList):
    if not tasksList:
        print("Nenhuma tarefa cadastrada.\n")
        return

    try:
        selectId = int(input("Selecione o ID da tarefa: "))
    except ValueError:
        print("❌ ID inválido.\n")
        return

    for task in tasksList:
        if task.id == selectId:
            if task.status:
                print("⚠️ Tarefa já concluída.\n")
                return

            task.status = True
            saveTasks(tasksList)
            print("✅ Tarefa concluída.\n")
            return

    print("⚠️ Tarefa não encontrada.\n")
