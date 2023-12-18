if __name__ == '__main__':
    import sys

def shelter_analysis(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file
    except:
        print("File not found")

ours_enters = 0
attack_theirs = 0
time_ours_in = 0
Longest_visit = 0
shortest_visit = 0

