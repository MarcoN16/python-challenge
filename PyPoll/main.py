
# Function for counting votes: 
#ls1: is unique list of candidate's name
#ls2: is the list of casting votes for each candidate

def counting(ls1,ls2,total_votes):
    candidates_vote = []
    for name in ls1:
        cand_name = name
        numb_vot = int(ls2.count(name)) 
        candidates_info = {'Candidate_Name': cand_name, '%Votes' : round((numb_vot/total_votes)*100,3), 'Votes' : numb_vot }
        candidates_vote.append(candidates_info)
    return candidates_vote

# votes analysis
import os
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    poll_file = csv.reader(csvfile, delimiter=',')
    csv_header = next(poll_file)
    total_votes = 0
    candidate_list = []
    candidate_votes = []

    # Read each row of data after the header
    for row in poll_file:
        total_votes += 1
        candidate_votes.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    cast_votes = counting(candidate_list,candidate_votes,total_votes)
    winner_votes = max(highest_votes['Votes'] for highest_votes in cast_votes)
    winner = [name['Candidate_Name'] for name in cast_votes if name['Votes']== winner_votes]


output_file = 'Election_Results.txt'
output_path = os.path.join("analysis", output_file)
with open(output_path, 'w') as outfile:

    summary = (
        "\n"
        "Election Results\n"
        "\n"
        "----------------------------\n"
        "\n"
        f"Total Votes: {str(total_votes)}\n"
        "\n"
        "----------------------------\n"
        "\n"
    )   
    print(summary)
    outfile.write(summary)

    for i in range(len(cast_votes)):

        all_candidates = f"{cast_votes[i]['Candidate_Name']}:  {cast_votes[i]['%Votes']}%  ({cast_votes[i]['Votes']})\n"
        print(all_candidates)
        outfile.write(all_candidates+"\n")
            
    TheWinner = (
        "\n"
        "----------------------------\n"
        "\n"
        f"Winner: {winner[0]}\n"
        "\n"
        "----------------------------\n"
    )
    print(TheWinner)
    outfile.write(TheWinner)

print(f"Election Results has been exported to '{output_file}'") 

