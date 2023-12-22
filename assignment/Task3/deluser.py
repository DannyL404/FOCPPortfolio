import sys

def deluser_program(password_file_path):
    try:
        with open(password_file_path, 'r+') as file:
            lines = file.readlines()
            selected_username = input("Please enter the username you would like to delete")
            for line_num, line in enumerate(lines, 1):
                if selected_username in line:
                    print("Match found!")
                    break
                else:
                    print("No username found")
    except:
        print("File not found")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print('There is no file selected!')
    else:
        deluser_program(sys.argv[1])