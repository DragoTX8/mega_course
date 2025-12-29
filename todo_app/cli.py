import functions as f


def main():
    f.clear_console()
    print(f"It is {f.return_current_time()}")

    # Reads the txt file or creates a blank file if one doesn't exists
    tasks = f.read_file_return_list("todos.txt")
    f.display_list_ordered(tasks)

    while True:
        user_action = input("Type add, complete, show, edit or exit: ").strip().lower()

        match user_action:
            case "exit":
                f.clear_console()
                f.display_list_ordered(tasks) if len(tasks) > 0 else None
                f.add_to_txt_file(tasks, "todos.txt")
                break

            case "add":
                user_task = input("Enter a todo: ").strip().lower()
                if user_task in tasks:
                    continue
                else:
                    f.add_to_list(tasks, user_task)

            case "complete":
                if len(tasks) == 0:
                    print("No tasks available for completing.")
                    continue
                else:
                    f.display_list_ordered(tasks)
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
                    completed = f.remove_from_list(tasks, to_remove)
                    print(f"{completed.title()} completed and removed from list.")

            case "edit":
                if len(tasks) == 0:
                    print("No tasks available for editing.")
                    continue
                else:
                    f.display_list_ordered(tasks)
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
                        f.add_to_list(tasks, new_task, to_edit - 1)

            case "show":
                if len(tasks) == 0:
                    print("There are no tasks to show.")
                    continue
                else:
                    f.display_list_ordered(tasks)

            case _:
                print(f"'{user_action}' is not a valid option.")


if __name__ == "__main__":
    main()
