import os #this imports the function that will let me open the file
# note for paul - I merged the second part of the question. I can display all three animals at once, that felt more efficient
def main():# the main function to open the files
    for file_name in os.listdir():# a for loop to open the files
        file_ptr = open(file_name) #making a variable to store the files
        file_ptr.readline() # this is to skip the first line 
        file_ptr.readline() # this is to skip the second line 
        file_ptr.readline() # this is to skip the third line 
        pass_to_GC_counter = GC_counter(file_ptr) # passing to something that can count the file bases
        print('The name of the file is',file_name,'and it has',pass_to_GC_counter,'GC bases') # the one that will take the return from the second function

def GC_counter(my_file): # a function to count the number of gcs
    my_GC = 0 # setting the counter
    for my_line in my_file: # loop through the argument
        my_line = my_line.strip() # strip the current object 
        my_line = list(my_line) # make the current line into a list
        for my_base in my_line: # go into the line list
            current = 0 # set counter
            current_base = (my_line[current]) # look up current base
            current += 1 # advance the counter
            if current_base == 'G' or current_base == 'C': # see if it is either g or c
                my_GC += 1 # add to count
    return my_GC # return function
main() # call the whole program