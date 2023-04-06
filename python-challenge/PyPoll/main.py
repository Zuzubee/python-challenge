# Julie

# Importing modules important for the analysis
import os
import csv

# Setting the path for csv file
data_path = os.path.join('Resources', "election_data.csv")

# A list to store the names of candidates
candidates = []

# A list to store the number of votes each candidate receives
num_votes = []

# A list to store the percentage of total votes each candidate
percent_votes = []

# A counter for storing the total number of votes
total_votes = 0

# Reading csv file
with open(data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Reading header row
    csv_header = next(csvreader)

    for row in csvreader:

        # Adding to our vote-counter
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    # Adding to percent_votes list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    # Finding the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# printing the output
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting the output to the text file
output_file = os.path.join('Analysis', 'PyPoll.txt')

pyPoll_output = open(output_file, "w")

line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
pyPoll_output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(
        f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    pyPoll_output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
pyPoll_output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
