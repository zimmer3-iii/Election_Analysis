# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base on popular vote.

#Add Dependencies
import csv 
import os 


#Assign a variable for the file to load and the path.

#file_to_load = 'Resources/election_results.csv'                    #Direct Method:
file_to_load = os.path.join("Resources", "election_results.csv")    #Indirect Method: Note you must have import for csv and os


#Open the election results and read the file.

#election_data = open(file_to_load, 'r')            #Method:1:
with open(file_to_load) as election_data:           #Method:2: 

#To do: perform analysis.

    print(election_data)

#Close the file.
election_data.close()


#WRITE TO FILES

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_anaylsis.txt")

#Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")          #Method:1
with open(file_to_save, "w") as txt_file:   #Method:2

    #Write some data to the file.
    #outfile.write("Hello World")           #Method:1
    txt_file.write("Counties in the Election\n------------------------\nArapahoen\nDenver\nJefferson")           #Method:2
    


#Close the file.
#outfile.close()                            #Method:1
txt_file.close()
