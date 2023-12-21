import sys


# function to read the log file from the command line argument
def shelter_analysis(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
    except:
        print("File not found")

#key variables
    ours_enters = 0
    theirs_attacks = 0
    time_ours_in_house = 0
    longest_visit = 0
    shortest_visit = 9999999999999
    total_visit_time = 0

    # stops the program if reading the line END
    for line in lines:
        if line == ('END'):
            break

        # Defines variables needed for the next if statement from the log file
        information = line.split(',')
        cat_type = information[0]
        entry_time = int(information[1])
        exit_time = int(information[2])

        # Runs checks against the log file to update variables for final output.
        if cat_type == 'OURS':
            ours_enters += 1
            total_visit_time = exit_time - entry_time
            time_ours_in_house += total_visit_time

            if total_visit_time > longest_visit:
                longest_visit = total_visit_time

            if total_visit_time < shortest_visit:
                shortest_visit = total_visit_time

        elif cat_type == 'THEIRS':
            theirs_attacks += 1

    average_visit_time = time_ours_in_house / ours_enters

    # Final program output
    print(f"Total number of times OUR cat entered the house: {ours_enters}")
    print(f"Number of times unwanted cats entered and were attacked: {theirs_attacks}")
    print(f"Total time spent in the house by OUR cat: {time_ours_in_house // 60} hours, {time_ours_in_house % 60} minutes")
    print(f"Average duration of each visit for OUR cat: {average_visit_time:.2f} minutes")
    print(f"Longest visit duration of OUR cat: {longest_visit} minutes")
    print(f"Shortest visit duration of OUR cat: {shortest_visit} minutes")



