import sys
import codecs

def passwd_program(password_file_path):
    try:
        with open(password_file_path, 'r') as file:
            lines = file.readlines()

            username = input("Enter your username: ")
            current_password = input("Enter your current password: ")
            current_password = codecs.encode(current_password, 'rot_13')

            for i, line in enumerate(lines):
                if username in line:
                    _, name, files_password = line.strip().split(':')
                    if current_password == files_password:
                        new_password = input("Enter a new password: ")
                        confirm_password = input("Enter your new password again: ")
                        if new_password == confirm_password:
                            new_password = codecs.encode(new_password, 'rot_13')
                            lines[i] = f"{username}:{name}:{new_password}\n"
                            with open(password_file_path, 'w') as file:
                                file.writelines(lines)
                            print("Password changed successfully.")
                        else:
                            print("Passwords do not match.")
                        return
                    else:
                        print("Incorrect password.")
                        return

            print("Username not found.")

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('There is no file selected!')
    else:
        passwd_program(sys.argv[1])
