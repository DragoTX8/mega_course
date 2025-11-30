import os


def add_to_list(existing_list: list, new_item, location=None) -> None:
    if location == None:
        existing_list.append(new_item)
    else:
        existing_list[location] = new_item


def display_list_ordered(task_list: list) -> None:
    for index, task in enumerate(task_list):
        print(f"{index + 1}. {task.title()}")


def clear_console() -> None:
    os.system("cls")


def main():
    clear_console()
    tasks: list = []

    while True:
        user_action = input("Type add, show, edit or exit: ").strip().lower()

        match user_action:
            case "exit":
                clear_console()
                display_list_ordered(tasks)
                break
            case "add":
                user_task = input("Enter a todo: ").strip().lower()
                if user_task in tasks:
                    continue
                else:
                    add_to_list(tasks, user_task)
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
                display_list_ordered(tasks)
            case _:
                print(f"'{user_action}' is not a valid option.")


if __name__ == "__main__":
    main()
