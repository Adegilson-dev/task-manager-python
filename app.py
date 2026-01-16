from storage import loadTasks
from services import addTask, listTasks, removeTask, completeTask

tasksList, currentId = loadTasks()

while True:
    option = input(
        "\nMenu\n"
        "1- Adicionar tarefa\n"
        "2- Exibir tarefas\n"
        "3- Remover tarefa\n"
        "4- Concluir tarefa\n"
        "5- Sair\n"
        "Escolha: "
    )

    match option:
        case "1":
            currentId = addTask(tasksList, currentId)
        case "2":
            listTasks(tasksList)
        case "3":
            removeTask(tasksList)
        case "4":
            completeTask(tasksList)
        case "5":
            print("👋 Saindo...")
            break
        case _:
            print("❌ Opção inválida.")
