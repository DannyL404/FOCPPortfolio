import sys
import codecs

def login_program(password_file_path):
    try:
        with open(password_file_path, 'r') as file:
            lines = file.readlines()

            username = input("Enter your username: ")
            password = input("Enter your password: ")
            password = codecs.encode(password, 'rot_13')

            for line in lines:
                if username in line:
                    _, _, files_password = line.strip().split(':')
                    if password == files_password:
                        print("Login Sucess!")
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
        login_program(sys.argv[1])
