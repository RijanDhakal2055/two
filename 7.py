Prime_list = [] # i did not use functions here, so this just the list that will store our answers 

number = int(input('Please enter the number up to which you want the list of prime numbers ')) # user input
for value in range(2, number+1): # loop that will go through the numbers upto and including user input
    for x in range(2,value): # nested loop
        if (value%x) == 0: # if value is divided by x, where x is loop until value so for example 7 is divided by every number until seven
            break # break if it is divisible, for example 9%3 == 0 is true so break
    else: # the other conditon that for the nested loop 
        Prime_list.append(value) # append the value to prime list
print('All the prime numbers in the list are',Prime_list)  # print result
