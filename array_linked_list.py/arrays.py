

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.elements = [None] * capacity

# Double the size of the given array
def resize_array(array):
    new_capacity = array.capacity * 2  #double is the best for new capacity
    new_elements = [None] * new_capacity

    for i in range(array.capacity):
        new_elements[i] = array.elements[i]

    array.elements = new_elements #updates all elements in array
    array.capacity = new_capacity #update size of array


# Return an element of a given array at a given index
def array_read(array, index):
    # Throw an error if array is out of the current count
    if index >= array.count: #capacity
        print ("Error! index " + str(index) + " out of range")
        return None
    
    return array.elements[index] # going to cheat a little and use a built in function here


# Insert an element in a given array at a given index
def array_insert(array, value, index):
    # Throw an error if array is out of the current count
    if index > array.count:
        print ("Error, index " + str(index) + " out of range") # you can't insert when there's an empty space ie [1,2,_,3], so need to raise error, checking if index is above the count
    # Resize the array if the number of elements is over capacity
    if array.capacity <= array.count:
        resize_array(array) # this will resize the old array right here

    # Move the elements to create a space at 'index' 
    # # Think about where to start!
    for i in range(array.count, index, - 1):
        array.elements[i] = array.elements[i-1] # shifts elements backward
   

    # Add the new element to the array and update the count
    array.elements[index] = value
    array.count += 1

# Add an element to the end of the given array
def array_append(array, value):
    # Hint, this can be done with one line of code
    # (Without using a built in function)
    array_insert(array, value, array.count)

# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove(array, element):
    for i in range(array.count):
        if removed:
            array.elements[i-1] == array.elements[i]
        elif array.elements[i] == element:
            removed = True
        
    if removed:
        array.count -= 1
        array.elements[array.count] = None
    else:
        print("Error, element" + str(element) + " not found")

# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop(array, index):
    # Throw an error if array is out of the current count
    if index > array.count:
        print("Error, index "+ stri(index)+ " is out of range")
        return None
    #what is the return value?
    return_value = array.elements[index]

    for i in range(index + 1, array.count):
        array.elements[i - 1] = array.element[i]

    array.count -= 1
    array.elements[array.count] = None
    return return_value


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


 
arr = array(1)
array_insert(arr, "STRING1", 0)
array_print(arr)
array_pop(arr, 0)
array_print(arr)
array_insert(arr, "STRING1", 0)
array_append(arr, "STRING4")
array_insert(arr, "STRING2", 1)
array_insert(arr, "STRING3", 2)
array_print(arr)
