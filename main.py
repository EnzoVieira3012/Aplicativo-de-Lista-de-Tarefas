class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Tarefa '{task}' adicionada com sucesso.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Tarefa '{removed_task['task']}' removida com sucesso.")
        else:
            print("Índice inválido.")

    def mark_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Tarefa '{self.tasks[task_index]['task']}' marcada como concluída.")
        else:
            print("Índice inválido.")

    def show_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa na lista.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Concluída" if task["completed"] else "Pendente"
                print(f"{index}. {task['task']} - {status}")

def main():
    manager = TaskManager()

    while True:
        print("\n1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Mostrar tarefas")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            task = input("Digite a tarefa: ")
            manager.add_task(task)
        elif choice == '2':
            task_index = int(input("Digite o índice da tarefa a ser removida: "))
            manager.remove_task(task_index)
        elif choice == '3':
            task_index = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
            manager.mark_as_completed(task_index)
        elif choice == '4':
            manager.show_tasks()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
