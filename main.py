from prompts import *


def get_items():
    with open('list_items.txt', 'r') as file:
        list_items = file.readlines()
    return list_items


def write_items(list_items):
    with open('list_items.txt', 'w') as file:
        file.writelines(list_items)


while True:
    user_action = input(action_prompt)
    command = user_action.split()[0].lower()
    if command == 'exit':
        break
    elif command == 'cl':
        print(command_list)
    elif command == 's':
        items = get_items()

        for index, item in enumerate(items):
            print(f"{index + 1}. {item}")
    elif command not in "ased":
        print(unknown_error)
    elif len(user_action.split()) < 2:
        print(command_error)
    else:
        user_input = ' '.join(user_action.split()[1].strip())
        match user_action[0].lower():
            case "a":
                item = user_input + "\n"

                items = get_items()

                items.append(item)

                write_items(items)
            case "e":
                index = int(user_input) - 1

                items = get_items()

                if 0 <= index < len(items):
                    item = items[index]
                    edited_item = input(f"Enter edit for {item}")
                    items[index] = edited_item + "\n"

                    write_items(items)
                    print(f"Changed '{item[:-1]}' to '{edited_item}'")
                else:
                    print(not_found_error)
            case "d":
                index = int(user_input) - 1

                items = get_items()

                if 0 <= index < len(items):
                    removed_item = items.pop(index)

                    write_items(items)

                    print(f"Removed '{removed_item[:-1]}' from list")
                else:
                    print(not_found_error)
            case _:
                print(unknown_error)
