def main(): # the main function that will bring everything together
    DNA_sequence_STR = input('Please enter the dna sequence here:- ').upper() # turn everything that is input into capital letters 
    DNA_sequence_list  = list(DNA_sequence_STR) # turns the user input into lists 
    count = len(DNA_sequence_STR) # to count the number of bases that the user passed in
    pass_to_compliment = compliment(DNA_sequence_list) # pass to the function that will count our bases
    current = 0 # the counter that I will later use to call bases in the list 
    number_of_A =0 # I do not know how to set counter without setting it to zero first
    number_of_T =0 # ^^^
    number_of_C =0 # ^^^
    number_of_G =0 # ^^^
    number_of_Invalid =0 # ^^^ 
    for base in range(0,count): # the loop that will parse through the list of bases
        current_base = (DNA_sequence_list[current]) # receives the counter and then opens the list at hand
        current += 1 # a way to add to the counter and make it advance
        if current_base == 'A':  # to check if the base is a 
            number_of_A +=1 # count it if it is indeed a 
        elif current_base == 'T': # ^^^
            number_of_T += 1 # ^^^
        elif current_base == 'C':# ^^^
            number_of_C += 1# ^^^
        elif current_base == 'G':# ^^^
            number_of_G += 1# ^^^
        else:# ^^^
            number_of_Invalid += 1# ^^^
    print('The number of bases A is ', number_of_A) # receives the number of A's count and prints it 
    print('The number of bases T is ', number_of_T)# ^^^
    print('The number of bases Cis ', number_of_C)# ^^^
    print('The number of bases G is ', number_of_G)# ^^^
    print('The number of bases that are invalid is ', number_of_Invalid)# ^^^

def compliment(list): # this is the one that actaully checks if it is the right function
    counter = len(list) # looking back this might have been redundant but this takes the argument
    current = 0 # to loop through the list
    compliment_list =[] # to receive the compliment base
    for current_base in range(0,counter): # the for loop to loop through the argument
        current_nucleotide = (list[current])
        current +=1
        if current_nucleotide == 'A': # takes the current arugment
            compliment_list.append('T')# assigns compliment
        elif current_nucleotide == 'T': # ^^^
            compliment_list.append('A')# ^^^
        elif current_nucleotide == 'C':# ^^^
            compliment_list.append('G')# ^^^
        elif current_nucleotide == 'G':# ^^^
            compliment_list.append('C')# ^^^
        else:
            compliment_list.append('Invalid base')
    print('This is your compliment list:-',compliment_list)  # ^^^

keep_going = 'y' # to let the user repeat the whole thing if need be
while keep_going == 'y':
    main()
    keep_going = input('Do you want to keep going, if so press Yes.')