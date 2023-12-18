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
total_visit_time = 0

for line in lines:
    if line == line.strip('END'):
        break

information = cat_type, entry_time, exit_time
entry_time = int(entry_time)
exit_time = int(exit_time)

if ours_enters == True:
    ours_enters += 1
    total_visit_time = exit_time - entry_time
    time_ours_in += total_visit_time