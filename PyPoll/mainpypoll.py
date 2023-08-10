# import the relavant modules
import os
import csv

# setting the terminal directory based on the current file path
current_file_path= os.path.abspath(__file__)
current_file_directory= os.path.dirname(current_file_path)
os.chdir(current_file_directory)

# create variables
total_votes=0

# create lists required to hold the data needed
candidate_options = []
candidate_votes ={}
result_dictionary={}
winner_count = 0
winner_percentage = 0

# defining the file path to read data
csvpath=os.path.join("pypollresources", "election_data.csv")

# opening and reading the given data file
with open(csvpath, newline='') as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvfile)
    
    # read through all the rows to calculate the total number of votes
    for row in csvreader:
        total_votes=total_votes+1

        # Adding candidates to the candidate list and counting votes for each candidate
        candidate_name= row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # counting votes for each candidate name
            # firstly, initialising the variable
            candidate_votes[candidate_name]=0
        # secondly, counting votes 
        candidate_votes[candidate_name] = candidate_votes[candidate_name]+1    

    # printing out the output to terminal
    print("Election Results")
    print("--------------------------------------------------------------")
    print(f'Total Votes: {total_votes}')
    print("--------------------------------------------------------------")


    for candidate in candidate_votes:
        # calculate the vote count and percentage of vote count for each candidate
        votes = candidate_votes[candidate]
        vote_percentage = ((votes) / (total_votes)) * 100

        # store it in a dictionary to print out into textfile 
        result_dictionary[candidate] = {"votes": votes,"vote_percentage": vote_percentage}
    
    
        # print out the ouput to terminal terminal.
        print(f"{candidate}: {vote_percentage:.3f}% ({votes:,})")


        # find and print the name of the winning candidate.
        if (votes > winner_count) and (vote_percentage > winner_percentage):
            winner_count = votes
            winner_candidate = candidate
           
    # Print the winner's name to the terminal.
    winner_candidate_name = (f"Winner: {winner_candidate}")

    print("--------------------------------------------------------------")        
    print(winner_candidate_name)
    print("--------------------------------------------------------------")
    

    # printing the output to a text file name pypoll_election_data
    file=os.path.join("pypollanalysis", "pypoll_election_data.txt")
    with open(file, "w") as output_file:

        output_file.write("Election Results\n")
        output_file.write("--------------------------------------------------------------\n")
        output_file.write(f'Total Votes: {total_votes}\n')
        output_file.write("--------------------------------------------------------------\n")  
        for candidate, result in result_dictionary.items():
            output_file.write(f"{candidate}: {result['vote_percentage']:.3f}% ({result['votes']}) \n")
        output_file.write("--------------------------------------------------------------\n")
        output_file.write(f'Winner: {winner_candidate}\n')
        output_file.write("--------------------------------------------------------------\n")