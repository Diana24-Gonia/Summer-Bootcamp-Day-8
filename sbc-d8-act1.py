def register(name):
    username = name[:10].lower()
    return username

def login(username, password):
    file = open("Login.txt", "a")
    file.write(f"{username},{password}\n")
    file.close()

def user_register():
    print("Welcome! Let's register you.")
    name = input("Please enter your name: ")
    username = register(name)
    password = input("Please create a password: ")
    login(username, password)
    print("Your login details have been saved.")

def change_password(username):
    print(f"Changing password for {username}")
    old_password = input("Enter your old password: ")
    new_password = input("Enter your new password: ")

    file = open("Login.txt", "r")
    lines = file.readlines()
    file.close()

    updated_lines = []
    found = False
    for line in lines:
        stored_username, stored_password = line.strip().split(',')
        if stored_username == username:
            if stored_password == old_password:
                updated_lines.append(f"{username},{new_password}\n")
                found = True
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)

    if not found:
        print("Username not found or incorrect old password. Password not changed.")
        return

    file = open("Login.txt", "w")
    file.writelines(updated_lines)
    file.close()

    print("Password changed successfully.")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file = open("Login.txt", "r")
    for line in file:
        stored_username, stored_password = line.strip().split(',')
        if stored_username == username and stored_password == password:
            print(f"Welcome, {username}!")
            file.close()
            return True

    file.close()
    print("Invalid username or password.")
    return False

def main():
    while True:
        print("Welcome to the login system.")
        print("1. Register \n2. Change password \n3. Login \n4. Exit")
        choice = input("Choose 1-4: ")

        if choice == '1':
            user_register()
        elif choice == '2':
            username = input("Enter your username: ")
            change_password(username)
        elif choice == '3':
            if login_user():
                print("Login successful.")
            else:
                print("Login failed. Please try again.")
        elif choice == '4':
            print("Exiting the program.")
            break  
        else:
            print("Invalid choice. Please choose again.")
main()
