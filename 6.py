def main(): # this will call the main and here the only function
    list_of_numbers = [23,22.7,4,5,67.3,34,3,4,1,1,2] # the assigned input 
    odd_total = 0 # a way to set up the count
    even_toal = 0 # ^^^
    for item in list_of_numbers: # the loop that will go through the assigned input 
        if int(item)%2 == 0: # to see if it is even 
            even_toal += item # to count what is even 
        elif int(item)%2 !=0: # to see if it is odd
            odd_total += item # to count if it is odd
    print('The total of all the odd number is ', odd_total) # display results
    print('The total of all the even number is ', even_toal) # diplay results

main() # call the main function 