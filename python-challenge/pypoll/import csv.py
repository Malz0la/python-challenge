import csv

file_to_load="election_data.csv"
file_to_output="analysis/election_analysis.txt"

#total vote counter
total_votes = 0

#candidate options and vote counters
candidate_options=[]
candidate_votes={}

#winning candidate and winning count tracker
winning_candidate=""
winning_count=0

#read in the csv and convery it into a list of dictionaries
with open(file_to_load) as election_data:
    reader=csv.DictReader(election_data)

    #for each row
    for row in reader:

        #add to total vote count
        total_votes=total_votes+1

        #extract the candidate name for each row
        candidate_name=row["Candidate"]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            #And begin tracking that candidates voter count
            candidate_votes[candidate_name]=0
        #then add vote to that candidate's count
        candidate_votes[candidate_name]=candidate_votes[candidate_name]+1

    # print the results and export the data to our text file
    with open(file_to_output, "w")as txt_file

        #print the final vote count
        election_results=(
            f"\n\nElection Results\n"
            f"------------------------\n"
            f"Total Votes:{total_votes}\n"
            f"-------------------------\n"
        )
        print(election_results)

        #save the final vote count to the text file
        txt_file.write(election_results)

        #determine the winner by looping through the counts
        for candidate in candidate_votes:

            #retrieve the vote count and percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100

            #determine winning vote count and candidate
            if(votes > winning_count):
                winning_count=votes
                winning_candidate=candidate

            #print each candidate's voter count and percentage
            voter_output=f"{candidate}: {voter_percentage:.3f}% ({votes})\n"
            print(voter_output)

            #save each candidate's voter count and percentage to txt file
            txt_file.write(voter_output)

        #print the winning candidate
        winning_candidate_summary=(
            f"-----------------\n"
            f"Winner: {winning_candidate}\n"
            f"------------------------\n"
        )
        print(winning_candidate_summary)

        #save the winning cadidate's name to the text file
        txt_file.write(winning_candidate_summary)