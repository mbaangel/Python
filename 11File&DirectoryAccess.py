"""
File and Directory Access
"""
import os

file_name = "moredev.txt"

with open(file_name, "w") as file:
    file.write("Angel Morales\n")
    file.write("36\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""
/*
* EXERCISE:
* Develop a program capable of creating a file that is called like
* your GitHub user and has the extension .txt.
* Add several lines to that file:
* - Your name.
* - Age.
* - Favorite programming language.
* Print the content.
* Delete the file.
*
* EXTRA DIFFICULTY (optional):
* Develop a sales management program that stores its data in a
* .txt file.
* - Each product is saved in a line of the file as follows:
* [product_name], [quantity_sold], [price].
* - Following this format, and through the terminal, it must allow adding, consulting,
* updating, deleting products and exiting.
* - It must also have options to calculate total sales and sales by product.
* - The exit option deletes the .txt.
*/
"""

file_name = "MoreDev_shop.txt"


open(file_name, "a")

while True:
    print("1. Add product.")
    print("2. Info product.")
    print("3. Update product.")
    print("4. Delete product.")
    print("5. Show products.")
    print("6. Gross Sale.")
    print("7. Sale by product.")
    print("8. Exit.")

    option = input("Select an option: ")

    if option == "1":
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
    
    elif option == "2":
        name = input("Name: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    
    elif option == "3":
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    
    elif option == "4":
        name = input("Name: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    
    elif option == "4":
        name = input("Name: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    
    elif option == "7":
        name = input("Name: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        
        print(total)
    
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Select an available option.")