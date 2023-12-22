import sys

def deluser_program(password_file_path):
    try:
        with open(password_file_path, 'r') as file:
            lines = file.readlines()
            selected_username = input("Please enter the username you would like to delete")
            included_lines = [line for line in lines if selected_username not in line]

        with open(password_file_path, 'w') as file:
            file.writelines(included_lines)

        if len(included_lines) < len(lines):
            print(f"{selected_username} has been successfully deleted.")
        else:
            print("No match found!")

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('There is no file selected!')
    else:
        deluser_program(sys.argv[1])
