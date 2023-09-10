CONTACTS_DICT = {}

# we create a function to handle errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError. Enter user name."
        except ValueError:
            return "ValueError. Enter user name and phone number please."
        except IndexError:
            return "IndexError. Enter user name and phone number please."
    return inner


# we create a decorator function to add a name and phone number to the dictionary
@input_error
def add_contacts(name, phone):
    if name in CONTACTS_DICT:
        raise ValueError
    CONTACTS_DICT[name] = phone
    return f"{name.title()} with number {phone} has been added."


# we create a decorator function to change the phone number by the specified name
@input_error
def change_phone(name, phone):
    if name not in CONTACTS_DICT:
        raise KeyError
    else:
        CONTACTS_DICT[name] = phone
        return f"Phone number for {name.title()} has been changed to {phone}."


# here we get the phone number from the entered name
@input_error
def get_phone(name):
    if name not in CONTACTS_DICT:
        raise KeyError
    return f"{name.title()}'s phone number is {CONTACTS_DICT[name]}."

# extract all contacts from our dictionary
@input_error
def show_all():
    if not CONTACTS_DICT:
        raise KeyError
    result = f"All contacts:\n"
    for name, phone in CONTACTS_DICT.items():
        result += f"{name.title()}: {phone} \n"
    return result


def hello():
    return "How can I help you?"


def end():
    return "Good bye :)"


# created a main function that accepts commands and uses other functions to process them
def main():
    while True:
        user_input = input("Enter a command: ").lower()
        user_separated = user_input.split(maxsplit=2)
        result_input = ""

        for char in user_input:
            if char != " ":
                result_input += char
            else:    
                break

        if user_input in ["hello", "hi", "aloha"]:
            print(hello())

        elif result_input == "add":
            if len(user_separated) < 3:
                print("Enter <add> <user_name> <phone_number> please.")
            else:
                print(add_contacts(user_separated[1], user_separated[2]))

        elif result_input == "change":
            if len(user_separated) < 3:
                print("Enter <change> <user_name> <phone_number> please.")
            else:
                print(change_phone(user_separated[1], user_separated[2]))

        elif result_input == "phone":
            if len(user_separated) < 2:
                print("Enter <phone> <user_name> please.")
            else:
                print(get_phone(user_separated[1]))

        elif user_input == "show all":
            print(show_all())

        elif user_input in ["good bye", "close", "exit"]:
            print(end())
            break

        else:
            print("Unknown command. Try it: 'hello', 'hi', 'aloha', add', 'change',"
                  " 'phone', 'show all', 'good bye', 'close', 'exit'.")
        

if __name__ == '__main__':
    main()
            

        





