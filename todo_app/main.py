import os


def read_file_return_list(file_path: str) -> list:
    """Opens text file and returns a list. Or creates one if one does not exist."""
    try:
        with open(file_path, "r") as f:
            return [task.rstrip() for task in f.readlines()]
    except FileNotFoundError:
        with open(file_path, "w") as f:
            pass
        return []


def add_to_list(existing_list: list, new_item, location=None) -> None:
    if location is None:
        existing_list.append(new_item)
    else:
        existing_list[location] = new_item


def remove_from_list(existing_list: list, index_to_remove: int):
    removed_task = existing_list.pop(index_to_remove - 1)
    return removed_task


def add_to_txt_file(items_to_add: list, file_name: str):
    with open(file_name, "w") as f:
        for item in items_to_add:
            f.write(f"{item}\n")


def display_list_ordered(task_list: list) -> None:
    for index, task in enumerate(task_list):
        print(f"{index + 1}. {task.title()}")


def clear_console() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    clear_console()

    # Reads the txt file or creates a blank file if one doesn't exists
    tasks = read_file_return_list("todos.txt")
    display_list_ordered(tasks)

    while True:
        user_action = input("Type add, complete, show, edit or exit: ").strip().lower()

        match user_action:
            case "exit":
                clear_console()
                display_list_ordered(tasks) if len(tasks) > 0 else None
                add_to_txt_file(tasks, "todos.txt")
                break

            case "add":
                user_task = input("Enter a todo: ").strip().lower()
                if user_task in tasks:
                    continue
                else:
                    add_to_list(tasks, user_task)

            case "complete":
                if len(tasks) == 0:
                    print("No tasks available for completing.")
                    continue
                else:
                    display_list_ordered(tasks)
                    to_remove = (
                        input("Enter the number of the task to be completed: ")
                        .strip()
                        .lower()
                    )
                try:
                    to_remove = int(to_remove)
                except ValueError:
                    print(f"{to_remove} is not a number.")
                    continue

                if to_remove > len(tasks):
                    print(f"There is no task with number {to_remove}")
                    continue
                else:
                    completed = remove_from_list(tasks, to_remove)
                    print(f"{completed.title()} completed and removed from list.")

            case "edit":
                if len(tasks) == 0:
                    print("No tasks available for editing.")
                    continue
                else:
                    display_list_ordered(tasks)
                    to_edit = (
                        input("Enter the number of the task to be edited: ")
                        .strip()
                        .lower()
                    )
                    try:
                        to_edit = int(to_edit)
                    except ValueError:
                        print(f"{to_edit} is not a number.")
                        continue

                    if to_edit > len(tasks):
                        print(f"There is no task with number {to_edit}")
                        continue
                    else:
                        new_task = (
                            input("What would you like the new task to be: ")
                            .lower()
                            .strip()
                        )
                        add_to_list(tasks, new_task, to_edit - 1)

            case "show":
                if len(tasks) == 0:
                    print("There are no tasks to show.")
                    continue
                else:
                    display_list_ordered(tasks)

            case _:
                print(f"'{user_action}' is not a valid option.")


if __name__ == "__main__":
    main()
