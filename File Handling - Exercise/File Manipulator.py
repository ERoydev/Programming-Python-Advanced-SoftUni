import os

while True:
    user_input = input()
    if user_input == "End":
        break

    args = user_input.split("-")
    command, file_name = args[0], args[1]

    if command == "Create":
        open(file_name, "w").close()

    elif command == "Add":
        content = args[2]

        with open(file_name, "a+") as file:
            file.write(content + "\n")


    elif command == "Replace":
        old_string = args[2]
        new_string = args[3]

        try:
            with open(file_name, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print("An error occurred")

        else:
            with open(file_name, "w") as file:
                content = content.replace(old_string, new_string)
                file.write(content)

    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)

        else:
            print("An error occurred")
