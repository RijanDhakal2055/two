import glob, os #the modules that I was missing 
from typing import Counter
import os.path          
from os import path     

def main():
    header_changes_knife = open('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\two\\10\\pauls_dna_seqs\\header_changes.csv','r') # the name of the csv file where the first column is the list of names of files and the third columns is the headers 
    # for i in header_changes_knife:
    firstColumn = [line.split(',')[0] for line in header_changes_knife] # makes a list of the first column of the header changes file, the name of the fasta file
    header_changes_knife.seek(0)
    third_column_read = [line.split(',')[2] for line in header_changes_knife] #makes a list of the third column of the header changes file, the new headers
    # for p in third_column_read:
        # print("{}\n".format(p))
    # my_pass_to_fasta_opener = my_fasta_opener(firstColumn) # passes the first column to the function that actually reads and opens the fasta files
    if path.exists('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\two\\10\\pauls_dna_seqs\\Updated_directory'):
        print("path exists")
    else:
        os.mkdir('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\two\\10\\pauls_dna_seqs\\Updated_directory') #need to make new directory for copy of the files
    counter = 0
    for my_new_dir in firstColumn:
        if "fasta" in my_new_dir:
            # print(my_new_dir)
            my_pass_to_fasta_opener = my_fasta_opener(my_new_dir) # passes the first column to the function that actually reads and opens the fasta files
            os.chdir('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\two\\10\\pauls_dna_seqs\\Updated_directory') #make the new directory for modified files
            # print(os.getcwd())
            # print("Open File {}".format(my_new_dir))
            make_new_file = open(my_new_dir,"w")# take the names from the csv first column and this is supposed to make a new file
            make_new_file.writelines(third_column_read[counter]) # takes the new header , that is what I meant to do here
            make_new_file.writelines(my_pass_to_fasta_opener) # receive the second line from the my_fasta_opener module
            make_new_file.close()
        else:
            print("not a valid fasta name {}".format(my_new_dir))
        counter += 1 
        

def my_fasta_opener(my_list): #this receives the names of the fasta files
    # counter = 0
    # for my_file in my_list:
    os.chdir('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\two\\10\\pauls_dna_seqs') #open fasta file directory
    print(my_list, os.getcwd())
    file_open = open(my_list) #open fasta files 
    file_open.readline() #read header but won't actaully do anything, a way to skip the header
    second_line = file_open.readline() # read the second line 
    return second_line #return the second line
        # counter += 1

            
main()