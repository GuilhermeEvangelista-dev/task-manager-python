tasks = []

def add_task():
    task = input("Digite a tarefa: ")
    tasks.append({"task": task, "done": False})
    print("Tarefa adicionada!")

def list_tasks():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")

def complete_task():
    list_tasks()
    num = int(input("Número da tarefa concluída: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
        print("Tarefa marcada como concluída!")

while True:
    print("\nGERENCIADOR DE TAREFAS")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    option = input("Escolha: ")

    if option == "1":
        add_task()
    elif option == "2":
        list_tasks()
    elif option == "3":
        complete_task()
    elif option == "4":
        break
