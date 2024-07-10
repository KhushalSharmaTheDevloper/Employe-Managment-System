import time as t
import random

def add():
    name = input("Enter Name: ")
    rank = input("Enter Rank: ")
    contact = input("Enter Number: ")

    print("Updating Details...")

    # Generate a unique passkey
    random_integer = random.randint(1, 1000000)
    passkey = str(random_integer)

    # Open the file in append mode
    with open("employe_data.txt", 'a') as f:
        f.write(f"Name: {name}, Rank: {rank}, Contact: {contact}, Passkey: {passkey}\n")
    t.sleep(1)
    print("Details Updated.")

def list_employees():
    try:
        with open("employe_data.txt", 'r') as f:
            read = f.read()
            print(read)
    except FileNotFoundError:
        print("No employee data found.")

def change_rank(name):
    lines = []
    found = False
    new_rank = input("Enter New Rank: ")

    with open("employe_data.txt", 'r') as f:
        lines = f.readlines()

    with open("employe_data.txt", 'w') as f:
        for line in lines:
            if line.startswith(f"Name: {name},"):
                parts = line.split(', ')
                parts[1] = f"Rank: {new_rank}"
                new_line = ', '.join(parts)
                f.write(new_line + '\n')
                found = True
            else:
                f.write(line)
    
    if found:
        print("Rank Updated.")
    else:
        print(f"No employee found with name {name}.")

def update_passkey(name):
    lines = []
    found = False
    new_passkey = str(random.randint(1, 1000000))

    with open("employe_data.txt", 'r') as f:
        lines = f.readlines()

    with open("employe_data.txt", 'w') as f:
        for line in lines:
            if line.startswith(f"Name: {name},"):
                parts = line.split(', ')
                parts[-1] = f"Passkey: {new_passkey}\n"
                new_line = ', '.join(parts)
                f.write(new_line)
                found = True
            else:
                f.write(line)
    
    if found:
        print("Passkey Updated.")
    else:
        print(f"No employee found with name {name}.")

def remove_employee(name):
    lines = []
    found = False

    with open("employe_data.txt", 'r') as f:
        lines = f.readlines()

    with open("employe_data.txt", 'w') as f:
        for line in lines:
            if not line.startswith(f"Name: {name},"):
                f.write(line)
            else:
                found = True
    
    if found:
        print(f"Employee {name} removed.")
    else:
        print(f"No employee found with name {name}.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Change Rank")
        print("4. Update Passkey")
        print("5. Remove Employee")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add()
        elif choice == '2':
            list_employees()
        elif choice == '3':
            name = input("Enter Name: ")
            change_rank(name)
        elif choice == '4':
            name = input("Enter Name: ")
            update_passkey(name)
        elif choice == '5':
            name = input("Enter Name: ")
            remove_employee(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
