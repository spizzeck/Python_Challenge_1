import csv
import os

file_to_load=os.path.join("Resources", "election_data.csv")
file_output=os.path.join("Analysis", "election_data.txt")
#Define Variables
total_votes=0
cand_options=[]
cand_votes={}
cand_results=[]
cand_win=[]
winner_votes = 0
win_percent=0
winning_count=0
votes = 0
vote_percentage=0
total_candidates = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header=next(reader)

# Add to the total vote count
    for row in reader:
        total_votes+=1
        cand_name=row[2]
#Add candidate name if not in options        
        if cand_name not in cand_options:
            cand_options.append(cand_name)
            cand_votes[cand_name] = 0
        cand_votes[cand_name] += 1
    for cand_name in cand_votes:
        votes = cand_votes.get(cand_name)
        vote_percentage = round(float(votes) / float(total_votes) * 100 , 2)
        cand_results += [(f"{cand_name}: {vote_percentage}% ({votes})")]
        if (votes > winning_count) and (vote_percentage > win_percent):
            winning_count = votes
            cand_win = cand_name
            win_percent = vote_percentage
#Generate Analysis Summary
Analysis = (
    f"Election Results\n"
    f"--------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------------------\n"
    f"Candidate Results: {cand_results}\n"
    f"--------------------------------\n"
    f"Winning Candidate: {cand_win} \n")
print(Analysis)

#Export to text file
with open(file_output, "w") as txt_file:
    txt_file.write(Analysis)