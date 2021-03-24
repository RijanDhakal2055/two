#This question is based on a real life problem and a common situation in data analysis. 
# You have a folder (directory) of fasta (DNA sequence) data files here. 
# (Note that the folder is a compressed zip file than you need to uncompress).  
# You also have a master spreadsheet (header_changes.csv) here. 
# Each fasta file has a header line, but these need to be changed. 
# Each row in header_changes.csv pertains to a file and the first item in that row is the file name. 
# Then a comma, then what should be the current header
#  (you might want to check to see if that is correct, and even deliberately insert one with the wrong header to make sure it can detect that!). 
# The third row is the new header name.
#  So your job is to replace the headers in all files correctly. 
# You might want to make sure that instead of writing over the old files, you save the new files in a new directory. 
# You can solve this in python, bash, or any combination of the 2.
#  You must include some documentation so that anyone else can run your code easily and understand what is going on.

import glob, os
from typing import Counter

def main():
    header_changes_knife = open('header_changes.csv','r') # the name of the csv file where the first column is the list of names of files and the third columns is the headers 
    for i in header_changes_knife:
        firstColumn = [line.split(',')[0] for line in header_changes_knife] # makes a list of the first column of the header changes file, the name of the fasta file
        header_changes_knife.seek(0)
        third_column_read = [line.split(',')[2] for line in header_changes_knife] #makes a list of the third column of the header changes file, the new headers
        my_pass_to_fasta_opener = my_fasta_opener(firstColumn) # passes the first column to the function that actually reads and opens the fasta files
        for my_new_dir in header_changes_knife:
            os.chdir('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\two\\10\\pauls_dna_seqs\\Updated directory')
            make_new_file = open(firstColumn,"w")
            make_new_file.writelines(firstColumn)
            make_new_file.writelines(third_column_read)
            

def my_fasta_opener(my_list):
    counter = 0
    for my_file in my_list:
        os.chdir('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\two\\10\\pauls_dna_seqs')
        file_open = open(my_list[counter])
        file_open.readline()
        second_line = file_open.readline()
        return second_line
        counter += 1

            
main()







