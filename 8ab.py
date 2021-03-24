def main():# the main function 
    list_of_lines = [] # the list that will hold the final answer 
    open_a_file = open('NENE01729A.txt','r') # the one specific file that it can open
    for read_a_line in open_a_file: # open file through a loop
        read_a_line = read_a_line.strip() # strip the lines
        list_of_lines.append(read_a_line) # send it to the list
    print(list_of_lines) # print list 

main() # call the function