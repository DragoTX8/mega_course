import time
import os


def return_current_time() -> str:
    epoch_time = time.time()
    current_time = time.ctime(epoch_time)
    return current_time


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
