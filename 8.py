import os # the module that I will need to import 

def second_part(): # this will take the path and open the file
    for file_name in os.listdir():# opens the path
        if file_name.startswith('NENE'): # opne the file it the name starts with NENE
            file_ptr = open(file_name) # set file pointer
            pass_to_mean = get_mean(file_ptr) # pass to the functon that will get us the mean
            # Reset file pointer to initial position
            file_ptr.seek(0) 
            pass_to_highest = get_highest(file_ptr) # pass to function that will get the highest number 
            # Reset file pointer to initial position
            file_ptr.seek(0)
            pass_to_lowest = get_lowest(file_ptr) # pass to function that will get the lowest 
            # Reset file pointer to initial position
            file_ptr.seek(0)
            pass_to_length_warning = get_length(file_ptr) # pass to function that will get the list 
            print('The name of the file is',file_name,'its highest value is',pass_to_highest,'its lowest value is',pass_to_lowest,'its mean is ',pass_to_mean,'and it is',pass_to_length_warning) # this is a bit wonky but this is what displays our results 

def get_mean(my_file): # the function that will get the mena
    my_list = []
    for my_line in my_file:
        my_line = my_line.strip()
        my_line = float(my_line)
        my_list.append(my_line)
    my_mean = sum(my_list)/len(my_list)
    return my_mean # return the mean to the running loop

def get_highest(my_file): # the funciton that will get the highest number
    my_list = []
    for my_line in my_file:
        my_line = my_line.strip()
        my_line = float(my_line)
        my_list.append(my_line)
    my_highest = max(my_list)
    return my_highest # return the mean to the running loop

def get_lowest(my_file): # the function that will get the lowest number
    my_list = []
    for my_line in my_file:
        my_line = my_line.strip()
        my_line = float(my_line)
        my_list.append(my_line)
    my_lowest = min(my_list)
    return my_lowest # return the mean to the running loop


def get_length(my_file): # the function that will get the length
    my_list = []
    for my_line in my_file:
        my_line = my_line.strip()
        my_line = float(my_line)
        my_list.append(my_line)
    length = len(my_list)
    x = 'This is not long enough'
    y = 'This is long enough'
    if length <= 300:
        return x # return the mean to the running loop if applicable 
    elif length >= 300:
        return y # return the mean to the running loop if applicable 
        
second_part() # call the main function 
