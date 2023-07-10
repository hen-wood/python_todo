from prompts import *

while True:
    user_action = input(action_prompt)
    match user_action.lower():
        case "cl":
            print(command_list)
        case "a":
            item = input("Enter an item: ") + "\n"

            file = open('list_items.txt', 'r')
            items = file.readlines()
            file.close()

            items.append(item)

            file = open('list_items.txt', 'w')
            file.writelines(items)
            file.close()
        case "s":
            file = open('list_items.txt', 'r')
            items = file.readlines()
            file.close()

            for index, item in enumerate(items):
                print(f"{index + 1}. {item}")
        case "e":
            index = int(input(edit_prompt)) - 1

            file = open('list_items.txt', 'r')
            items = file.readlines()
            file.close()

            if 0 <= index < len(items):
                item = items[index]
                edited_item = input(f"Enter edit for {item}")
                items[index] = edited_item + "\n"
                file = open('list_items.txt', 'w')
                file.writelines(items)
                file.close()
                print(f"Changed '{item[:-1]}' to '{edited_item}'")
            else:
                print(not_found_error)
        case "d":
            index = int(input(delete_prompt)) - 1

            file = open('list_items.txt', 'r')
            items = file.readlines()
            file.close()

            if 0 <= index < len(items):
                removed_item = items.pop(index)
                file = open('list_items.txt', 'w')
                file.writelines(items)
                file.close()
                print(f"Removed '{removed_item[:-1]}' from list")
            else:
                print(not_found_error)
        case _:
            print(unknown_error)
