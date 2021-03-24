def main(): # the function that will call the counter function 
    Sentence = input('Please enter the sentence that you want the program to work on:- ').upper() # this takes user input but in all caps
    sentence_list = Sentence.split() # this will make a list of all the words in the sentence
    count = counter(sentence_list) # this passes the the list to the counter function

def counter(words): # this is a function that will take the word list argument
    counter =0 # to set up the loop
    for words_1 in words: # the for loop that will go through the loop
        if words_1 == 'THE': # to check if the received word is the
            counter += 1 # advance the counter
    print('The sentence that you gave me has',counter,'instances of "THE"') # show results

main() # call the main function