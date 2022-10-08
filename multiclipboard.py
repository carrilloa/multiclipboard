import sys
import clipboard
import json

saved_data = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(saved_data)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(saved_data, data)
        print("Data saved. ")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard. ")
        else:
            print("Key does not exist. ")
    elif command == "list":
        print(data)
    elif command == "clear":
        check = input("Are you sure? Y/N: ")
        print("")
        if check == "Y" or check == "y":
            data = {}
            save_data(saved_data, data)
            print("Data cleared. ")
        elif check == "N" or check == "n":
            print("Data not cleared. ")
        else:
            print("Invalid command. ")
    elif command == "delete":
        key = input("Enter a key: ")
        if key in data:
            data.pop(key)
            save_data(saved_data, data)
            print("Key deleted. ")
        else:
            print("Key does not exist. ")
    else:
        print("Unknown Command")

else:
    print("Please type only 1 valid command. ")