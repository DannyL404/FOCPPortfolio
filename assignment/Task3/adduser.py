import sys
import codecs

def adduser_program(password_file_path):
    try:
        with open(password_file_path, 'r') as file:
            lines = file.readlines()
            new_username = input("Please enter the username you would like to add")
            for line in lines:
                if new_username in line:
                    print('Username in use!')
                    return
        fullname = input("Please enter your full name.")
        password = input("Please enter your password")
        password = codecs.encode(password, 'rot_13')

        new_line = ['\n' ,new_username, ':', fullname, ':' , password]
        new_list = lines + new_line
        with open(password_file_path, 'w') as file:
            file.writelines(new_list)


    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('There is no file selected!')
    else:
        adduser_program(sys.argv[1])

