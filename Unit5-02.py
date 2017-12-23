
# Created by: Scarlett Gao
# Created on: Nov 2017
# Created for: ICS3U
# This program displays finding the maximum value in array

from numpy import random

my_numbers = []

def greatest_value(array):
    # find the maximum value in array
    print('There are 10 random numbers:')
    
    # generate 10 random numbers
    for number in range(10):
        my_numbers.append(random.randint(1,100))
        print (my_numbers[number])
    
    # the maximum value
    # array_max = max(my_numbers)
    array_max = array[]
    
    for a_value in my_numbers:
        if array_max == 0:
            array_max = a_value
        elif array_max < a_value :
              array_max = a_value
        else:
          array_max = array_max
          
    return array_max

return_value = greatest_value(my_numbers)
print ('The greatest value in the array is: ' + str(return_value))
