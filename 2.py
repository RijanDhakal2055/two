from datetime import date #This imports the appropriate module

def main(): #the main module to get the code started
    print('Enter the starting date below in a stepwise manner as the computer asks for it') #telling the user what to do
    start_year = int(input('Please enter the starting year ')) #Taking the starting year
    start_month = int(input('Please enter the starting month ')) #taking the starting month
    start_day = int(input('Please enter the starting day '))#taking the starting day
    starting_date = date(start_year,start_month,start_day) # passing the staring date in the appropriate format to the date and time module 
    print('Enter the end date below in a stepwise manner as the computer asks for it')#telling the user what to do
    end_year = int(input('Please enter the ending year ')) #Taking in the ending year
    end_month = int(input('Please enter the ending month ')) #taking in the ending month
    end_day = int(input ('Please enter the ending day ')) #Taking in the ending day
    end_date = date(end_year,end_month,end_day) # passing the end date in the appropriate format to the date and time module 
    pass_to_difference = difference(starting_date,end_date) #Passing all of the data to the difference module
    print('The time between these two dates is', pass_to_difference,'days. Please note that this program calculates the number of days in between dates regardless of which date comes first.') # Taking the return data and printing it 

def difference(start,finish): #the module that calculates the difference
    time_between = finish - start #the command to calculate the difference
    answer = time_between.days #turning it into time
    day_count = abs(answer) #making the date positive
    return day_count #passing back the asnwer

main() #calling the program