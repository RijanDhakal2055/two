def main(): #This is just the main function of the overall program
# I do not like making a lot varables in my program and do not really mind using the same names as local varaibles.
# This is of course just opinion but I think it reduces clutter
    the_number = float(input('Please enter the number that we will be working on:- ')) # A line to take in the number that we will be working on
    pass_circle_area = area_of_circle(the_number) #This passes the number to the function the finds the area of the circle
    print('The area of the circle is ',pass_circle_area,'\n') #This just takes the value from the return function and prints it
    pass_circle_circumference = circumference_of_circle(the_number) #This passes the number to the function the finds the circumference of the circle
    print ('The circumference of the circle is ',pass_circle_circumference,'\n') #This just takes the value from the return function and prints it
    pass_area_of_square = area_of_square(the_number) #passes to the fucntion that calculates the area of the square
    print('The area of a square whose sides are ',the_number,'long will have area ',pass_area_of_square,'\n')#This takes the value from the return function to print the area of the square
    pass_factorial = factorial(the_number) #The command to pass the function to the factorial module
    print('The factorial of the number',the_number,'is',pass_factorial,'\n') #This takes the value from the return fuction and prints it in human redable form
    pass_power = self_power(the_number)# This passed the value to the module        
    print('IF you raise',the_number,'to the power of',the_number,'the answer will be',pass_power,'\n') #This prints the value from the return fucntion in human readable form

def area_of_circle(radius): #The one that deals with the defensive programming assignment
    if radius <= 0: #The command to check if the input is valid
        print('The number must be a positive value, circles do not have negative radius!')
    elif radius >0:
        area = (22/7)*radius*radius
        return area

def circumference_of_circle(radius): #The module that finds the circumference of the circle
    if radius <=0: #The command to check if the input is valid
        print('The number must be a positive value, circles do not have negative radius!')
    else:
        circumference = 2* (22/7)*radius
        return circumference #The command to return the answer

def area_of_square(side_length): # The command to find the area of the square
    if side_length <=0: #The command to check if the number is valid
        print('The number must be a positive value, sqaures do not have negative sides!')
    else:
        area = side_length * side_length
        return area #The command to return the answer to the main module

def factorial(number): #The module that calculates the factorial of the number
    if number <=0: #The command to check if the number is valid
        print('The number must be a positive value, negative numbers do not have negative factorials!')
    else:
        value = int(number)
        final =1
        for count in range(1,value+1):
            final =count*final
            if count == value:
                return final #The command to return the value to the main module

def self_power(number):#The module that calculates the answer to the number to the power of the number itself
    value = number ** number
    return value #The command that returns a value to the main module

keep_going = 'y' #The set up to ask the user if he wants to do the calculations with more numbers
while keep_going == 'y':
    main() #The most important command in the whole program
    keep_going = input('Press Y if you want to do this again ')
