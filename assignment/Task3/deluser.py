import sys

def deluser_program(password_file_path):
    try:
        with open(password_file_path, 'r+') as file:
            lines = file.readlines()
            selected_username = input("Please enter the username you would like to delete")
            for line_num, line in enumerate(lines, 1):
                if selected_username in line:
                    print("Match found!")
                    return selected_username
            print("No username found")
            return None
    except:
        print("File not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('There is not file selected!')
    else:
        username_match = deluser_program(sys.argv[1])
        if username_match is not None:
            print(username_match)
        else:
            print("No username matched.")
