Assigned_list = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0], # the varible that will hold the list
['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
['D5', 98], ['D6', 32]]
print('The number of sites is',len(Assigned_list)) # this will print the number of list we have
item_seven = Assigned_list[6] # The one that will print the seventh item in the list
last_site = Assigned_list[-1] # the one that will print the last item in the 
print('The number of salamander on the seventh site is',item_seven[1]) # since the seventh item itself is a list we can just take the second item
print('The number of salamanders that were counted at the last site is ',last_site[-1]) # same logic as the one that we used for the precious question

current = 0 # setting the list counter loop
total_salamanders = 0 # the varible for the total number of salamanders
for site in range(0,len(Assigned_list)): # the loop that will loop through the loop list itself
    current_site = Assigned_list[current] # open the current list item from the main list
    current += 1 # to make the counter proceed 
    current_site_count = current_site[1] # take the current item as the list and take the second item itself
    total_salamanders += current_site_count # add to the total count
print('The total number of salamanders is', total_salamanders) # print tht total
Average_number_of_salamanders = total_salamanders / (len(Assigned_list)) # this will give us the mean
print('The average number of salamanders is',Average_number_of_salamanders)

current_site_number_for_c = 0 # a loop for the c site
c_site_total = 0
for c_site in range (0,len(Assigned_list)):# this  loop will open the c sites
    current_c_site = Assigned_list[current_site_number_for_c]
    current_site_number_for_c += 1
    Alphabet = current_c_site[0] # takes the site small list
    Count_for_C = current_c_site[1] # takes the count 
    letter = Alphabet[0]
    if letter == 'C': # to check if the received varable is c 
        c_site_total += Count_for_C # adds to the c total
print('The total number of salamanders across the C sites is',c_site_total)




