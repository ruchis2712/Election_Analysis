####################################################################################
# ######### PyPoll.py analyzes Colorado election results from a csv file to  #######
# ######### give the total votes, county-wise votes, candidate-wise votes    #######
# ######### and vote%, as well as the largest county turnout and the winner  #######
####################################################################################

# Add dependencies
import csv
import os

# Assign a variable for the path where the files will be read from and written to
filepath = "C:/Users/rusinghal/Desktop/Berkley Extension docs/Class Work/Python"

# Assign variables for 'read and write' file names
pollfname="election_results.csv"
resultsfname="election_analysis.txt"

# Assign variable to load the files from/to the path
file_to_load=os.path.join(filepath,pollfname)
file_to_write=os.path.join(filepath,resultsfname)

#######################################################
# Initialize variables, arrays & Dictionaries
#######################################################

# A total vote counter
total_votes=0

# Candidate options and candidate votes
candidate_names=[]
candidate_votes={}

# County options and county votes
county_names=[]
county_votes={}

# Track the winning candidate, vote count, and percentage
winning_name=""
winning_votes=0
winning_percent=0

# Track the winning county, and vote count
winning_county=""
winning_county_votes=0

#######################################################

# Open the election results and read the file

with open(file_to_load,'r') as file_read:
    file_data=csv.reader(file_read)
    
    # Read and skip the header row
    headers=next(file_data)

    # Read each data row of the file
    for row in file_data:
        # Add to the total vote count
        total_votes += 1

        # Get the candidate and county name from each row
        candidate=row[2]
        county=row[1]

        # If the candidate does not match any existing candidate add it the
        # the candidate list
        if candidate not in candidate_names:
            # Add the candidate name to the candidate list
            candidate_names.append(candidate)
            # And begin tracking that candidate's voter count
            candidate_votes[candidate]=0
        
        # If the county does not match any existing county add it the
        # the county list
        if county not in county_names:
            # Add the county name to the county list
            county_names.append(county)
            # Begin tracking the county's voter count
            county_votes[county]=0
        
        # Add a vote to that candidate's and county's count
        candidate_votes[candidate]+=1
        county_votes[county]+=1

# Create message to write/print to results file. Print Total Vote count
msg_to_prn=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:"
    )

# Retrieve vote count and percentage for each county
for cnt in county_votes:
    cvotes=county_votes[cnt]
    cpercent=(cvotes/total_votes)*100
    
    # Check if the county has the largest turnout
    if cvotes>winning_county_votes:
        winning_county_votes=cvotes
        winning_county=cnt
    # Print each county, their voter count, and percentage
    msg_to_prn+=(f"{cnt}: {cpercent:.1f}% ({cvotes:,})\n")

# Print the largest turnout county name
msg_to_prn += (f"\n-------------------------------------\n")
msg_to_prn += (f"Largest County Turnout: {winning_county}\n")
msg_to_prn += (f"-------------------------------------\n")

for c in candidate_votes:
    votes=candidate_votes[c]
    percent=(votes/total_votes)*100
    
    # Check if the candidate has the highest number and % of votes and is the winner
    if votes>winning_votes and percent>winning_percent:
        winning_votes=votes
        winning_percent=percent
        winning_name=c
    # Print each candidate, their voter count, and percentage
    msg_to_prn+=(f"{c}: {percent:.1f}% ({votes:,})\n")

# Print the winning candidates' results
msg_to_prn += (f"-------------------------------------\n")
msg_to_prn += (f"Winner: {winning_name}\n")
msg_to_prn += (f"Winning Vote Count: {winning_votes:,}\n")
msg_to_prn += (f"Winning Percentage: {winning_percent:.1f}%\n")
msg_to_prn += (f"-------------------------------------\n")

# Print results to the terminal
print(msg_to_prn)

# Save the results in a text file
with open(file_to_write,'w') as results_file:
    results_file.write(msg_to_prn)

###########################   End of Code    ######################################