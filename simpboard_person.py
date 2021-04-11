# Author: Samuel Baker
# Date Created: 2/19/2021
# Date Finished: 2/19/2021

class Person:

    def __init__(self, name, aggregate):
        self.name = name
        self.aggregate = aggregate

def person_bubble_sort(arr, size):
    swapped = False
    for i in range(0, size - 1):
        if swapped == True:
           break
        swapped = True
        for  j in range(0, size - 1 - i):
            # This sorts from high to low
            if arr[j].aggregate < arr[j+1].aggregate:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = False


    