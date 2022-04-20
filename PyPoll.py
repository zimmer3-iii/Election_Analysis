# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base on popular vote.
# 6. Save results to Text file.

#Add Dependencies
import csv 
import os 


#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")    

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

#1.1 Initialize a total vote counter.
total_votes = 0
#2.1 Initialize Candidate List
candidate_options = []
#3.1 Initialize Candidate Vote Dictionary
candidate_votes = {}
#5.1 Determine Winning Candidate Variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0    

    
#Open the election results and read the file.
with open(file_to_load) as election_data:
    
    #Read the file object with the read function.
    file_reader = csv.reader(election_data )
    
    #Read the header row.
    headers = next(file_reader)

    #Iterate each row in the CSV file.
    for row in file_reader:
        
        #1.2 Add to the total vote count.
        total_votes += 1
        #2.2 Get the candidate name from each row. [2] is referencing the column in that row
        candidate_name = row[2]
            
        #2.3 Add the candidate name to list if not in list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #3.2 Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        #3.3 Count votes
        candidate_votes[candidate_name] += 1

    #6.1 Save to Text File
    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        #6.2 
        # Print the final vote count to the terminal.
       # Print the final vote count to the terminal.
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        #4.1 Determine the percentage of votes for each candidate by looping through the counts.
        ##Iterate through list 
        for candidate_name in candidate_votes:
            #4.2 Retrive vote count of a candidate
            votes = candidate_votes[candidate_name]
            #4.3 Calculate the percentage of votes.
            vote_percentage = float(votes)/float(total_votes)*100
            #4.4 Print Vote Percentage.
            #6.3 Writing Vote to File
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)
            

            #5.2 Comparasion

            if(votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

    

        #5.3 Print Winner.
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)
        #6.4 Writing winning candidate to text file.
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)

    #1.3 Print the total votes.
    #print(total_votes)
    #2.4 Print candidate list
    #print(candidate_options)
    #3.4 Print votes
    #print(candidate_votes)
