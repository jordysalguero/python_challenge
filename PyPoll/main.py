import os 
import csv

candidate = []
candidate_name = []
candidate_votes = []

electioncsv = os.path.join('Homework','Homework_#3','python_challenge','PyPoll','election_data.csv')

with open (electioncsv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]

    total_votes = len(candidate)

    for row in candidate_count:
        candidate_name.append(row[0])
        candidate_votes.append(row[1])
        winner = max(candidate_votes)

    candidate_info_zip = zip(candidate_name,candidate_votes)
    candidate_list = list(candidate_info_zip)

    for row in candidate_list:
        if row[1] == winner:
            name_of_winner = row[0]

    khan_total = candidate.count('Khan')
    khan_percentage = khan_total / total_votes

    correy_total = candidate.count('Correy')
    correy_percentage = correy_total / total_votes

    li_total = candidate.count('Li')
    li_percentage = li_total / total_votes

    otooley_total = candidate.count("O'Tooley")
    otooley_percentage = otooley_total / total_votes

output_path = os.path.join('.','Homework','Homework_#3', 'python_challenge','PyPoll','SummaryPoll.txt')
with open(output_path,'w',newline='') as summarytext:
    text_writer = csv.writer(summarytext)
    text_writer.writerow([f'Election Results'])
    text_writer.writerow([f'-------------------------'])
    text_writer.writerow([f'Total Votes: {total_votes}'])
    text_writer.writerow([f'-------------------------'])
    text_writer.writerow([f'Khan: {khan_percentage:.3%} ({khan_total})'])
    text_writer.writerow([f'Correy: {correy_percentage:.3%} ({correy_total})'])
    text_writer.writerow([f'Li: {li_percentage:.3%} ({li_total})'])
    text_writer.writerow([f"O'Tooley: {otooley_percentage:.3%} ({otooley_total})"])
    text_writer.writerow([f'-------------------------'])
    text_writer.writerow([f'Winner: {name_of_winner}'])
    text_writer.writerow([f'-------------------------'])

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percentage:.3%} ({khan_total})')
print(f'Correy: {correy_percentage:.3%} ({correy_total})')
print(f'Li: {li_percentage:.3%} ({li_total})')
print(f"O'Tooley: {otooley_percentage:.3%} ({otooley_total})")
print(f'-------------------------')
print(f'Winner: {name_of_winner}')
print(f'-------------------------')