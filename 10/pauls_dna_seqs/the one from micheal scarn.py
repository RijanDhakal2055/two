import os.path       # needed to use path.exists
from os import path  # needed to use path.exists
datafile_path = 'C:/Users/bmcec/OneDrive/Documents/pauls_dna_seqs/'  # gives permanate path to the ,fast dir
hdr_path = 'C:/Users/bmcec/OneDrive/Documents/header_changes.csv'    #gives permanate path to the csv with header changes
h_change = open(hdr_path) #opens csv and makes variable for the csv data

for line in (h_change):         #reads each line in csv 
    info = line.split(",")      #splits lines seperated by comma
    if 'fasta' in info[0]:      #checks if fasta is in first coloumn to skip header
        file_path = ("{}{}".format(datafile_path, info[0])) #uses info from csv to make file path to fasta files
        if path.exists(file_path):      #does file path made on line above exist in dir
            data = open(file_path, "r") #if it does it opens the file
            lines = data.readlines()    #reading info from fasta files
            if lines[0].strip() != info[1]: #if the header from fasta does not match old header in csv
                print("header does not match. needs to be corrected")    #alerts user 
            lines[0] = info[2]      #takes fasta header and replaces with csv new header
            with open(file_path, "w") as fp_out:    #opens file to write
                fp_out.writelines(lines)    #writes new header
        else:
            print("\nfile not found.\n".format(file_path)) #if error above alerts user
#testing
ninenine = open('C:/Users/bmcec/OneDrive/Documents/pauls_dna_seqs/99.fasta')
for lines in ninenine:
    print(lines)