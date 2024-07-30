'''  Structures '''

# List
my_list: list = ["More", "Black", "Wolfy", "Visions"]
print(my_list)
my_list.append("Castor") #Insertion
my_list.append("Castor")
print(my_list)
my_list.remove("More") # Elimination
print(my_list)
print(my_list[1])
my_list[1] = "Cuervillo" # Update
print(my_list)
my_list.sort() # Sorted
print(my_list)
print(type(my_list))

# Tuple
my_tuple: tuple = ("More", "@angel", "MoreDev", "36")
print(my_tuple[1]) # Access
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Sorted
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"More", "Angel", "@Angel", "36"}
print(my_set)
my_set.add("moredev@hotmail.com") # Insertion
my_set.add("moredev@hotmail.com")
print(my_set)
my_set.remove("More") # Elimination
print(my_set)
my_set = set(sorted(my_set)) # Can't sorted
print(my_set)
print(type(my_set))

# Dictionaries
my_dict: dict = {
    "Name": "Angel",
    "Surname": "Morales",
    "Alias": "@angel",
    "Age": "36"
}
my_dict["email"] = "moredev@hotmail.com" # Insertion
print(my_dict)
del my_dict["mbaangel"] # Elimination
print(my_dict)
print(my_dict["Name"]) # Access
my_dict["Age"] = "37" # Update
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Sorted
print(my_dict)
print(type(my_dict))

''' EXTRA '''
'''
* EXERCISE:
 * - Shows examples of creating all the structures supported by default in your language.
 * - Uses insert, delete, update and sort operations.
 *
 * EXTRA DIFFICULTY (optional):
 * Create a contact book per terminal.
 * - You must implement search, insert, update and delete contact functionalities.
 * - Each contact must have a name and phone number.
 * - The program first asks what operation you want to perform, and then
 * the data necessary to carry it out.
 * - The program cannot allow you to enter non-numeric phone numbers with more than 11 digits.
 * (or whatever number of digits you want)
 * - A program termination operation must also be proposed.
 '''

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Please enter the phone: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) == 10:
            agenda[name] = phone
        else:
            print("You must enter a 10-digits phone number.")
    
    while True:
        print("")
        print("1. Search contact")
        print("2. Insert contact")
        print("3. Update phone")
        print("4. Delete contact")
        print("5. Show all contacts")
        print("6. Exit")

        option = input("\nSelect an option: ")

        match option:
            case "1":
                name = input("Enter the contact name to search: ")
                if name in agenda:
                    print(
                        f"The phone number of {name} is {agenda[name]}."
                    )
                else:
                    print(f"The {name} contact is not exist.")
            case "2":
                name = input("Enter the contact name: ")
                insert_contact()
            case "3":
                name = input("Enter the contact name to update: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"The contact {name} is not exist.")
            case "4":
                name = input("Enter the contact name to erase: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"The {name} contact is not exist.")
            case "5":
                if agenda:
                    print("Contacts: ")
                    for name, phone in agenda.items():
                        print(f"{name}: {phone}")
                else:
                    print(f"No contacts found.")
            case "6":
                print(f"Exit from agenda.")
                break
            case _:
                print("Invalid option. Please choose an option from 1 to 6.")

my_agenda() 