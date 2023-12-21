import sys

#function to read the log file from the command line argument
def shelter_analysis(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
           lines = file.readlines()
    except:
        print("File not found")

# key variables
ours_enters = 0
attack_theirs = 0
time_ours_in = 0
longest_visit = 0
shortest_visit = 0
total_visit_time = 0

# stops the program if reading the line END
for line in lines:
    if line == line.strip('END'):
        break

# Defines variables needed for the next if statement from the log file
information = cat_type, entry_time, exit_time
entry_time = int(entry_time)
exit_time = int(exit_time)

# Runs checks against the log file to update variables for final output.
if ours_enters == True:
    ours_enters += 1
    total_visit_time = exit_time - entry_time
    time_ours_in += total_visit_time

if total_visit_time > longest_visit:
    total_visit_time = longest_visit

if total_visit_time < shortest_visit:
    total_visit_time = shortest_visit

elif attack_theirs == True:
    attack_theirs += 1

average_visit_time = total_visit_time / ours_enters

# Final program output
if ours_enters == 0:
    print("The cat did not enter today")

else:
    print(f"OUR cat entered {ours_enters} times.")
    print(f"Other cats entered and were attacked {attack_theirs} times.")
    print(f"OUR cat spent {time_ours_in} minutes in the house.")
    print(f"OUR cat was in the house for an everage of {average_visit_time} minutes.")
    print(f"The longest of these visits was {longest_visit}.")
    print(f"The shortest of these visits was {shortest_visit}.")