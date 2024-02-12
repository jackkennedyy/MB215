"""
#Activity 1. Define a list with different types of elements

my_list = [1, "two", 3.0, True] ###What this line of code does is create a list with an integer, string, float, and boolean. I can tell it's a list because of the square brackets
# Print the entire list
print("The entire list:", my_list) ###This would print the list created in the line prior
# Convert a tuple to a list using the list() function
#Tuples are defined by enclosing the elements within parentheses () instead of square brackets [] used by lists.
my_tuple = (4, "five", 6.0, False) ###This line creates a tuple with an integer, string, float, and boolean. I can tell it's a tuple because of the round brackers
tuple_to_list = list(my_tuple) ###This line converts the given tuple into a list so changes can be made
# Print the converted list
print("Converted list from tuple:", tuple_to_list) ###Prints my converted list



##Activity 2. repetitions over lists
# Define a simple list

simple_list = ['a', 'b', 'c'] ###Defines a simple list using only strings
# Use the repetition operator to make three copies of the list and join them together
repeated_list = simple_list * 3 ###Prompts the list to be repeated 3 times in the terminal
# Print the new list created by the repetition operator
print("Repeated list:", repeated_list)###Prints repeated list back to the user
# Iterate over the repeated list using a for loop and print each element
for element in repeated_list: ###Prints each element in the list to be repeated 3 times, all in seperate lines
    print(element)


##Activity 3. Index in lists
my_list = [10, 20, 30, 40, 50]###Creates a list using integers
element_to_find = 30 ###locates a specific element in the list

if element_to_find in my_list:
    index = my_list.index(element_to_find)
    print(f"The element {element_to_find} is at index {index}.")###Tells user where the given input is in the list
else:
    print(f"The element {element_to_find} is not in the list.")###Tells user that given input is not in the list

# we also can Print particular index value
print (f"The value at index 0 is {my_list[0]}.") ###Tells the user where a specific value is placed
##Print the length of the lest using len()
print(f"The length of the list is {len(my_list)}.")###Tells the user how long the list is (how many items are included)
# Change an element value in the list
newElement_value= my_list[0]=999###Changes a specific element in list
print("The new list fatre the change is:", my_list)###Prints back to user



##Activity 4 Concatenating lists using the + operator

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2 ###Combines two lists and turns them into a conjoined one
print("Concatenated list using + operator:", concatenated_list)

# Concatenating lists using the += augmented assignment operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 += list2
print("Concatenated list using += operator:", list1)###Does the same thing as the previous lines but in a different fashion

# Attempting to concatenate a list with a number (will result in an error)
list1 = [1, 2, 3]
number = 4 
# Uncomment the line below to see the error
##concatenated_list = list1 + number
"""
"""
##Activity 5. List Slicing

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic list slicing without specifying start or end
basic_slice = my_list[2:6] ###Prompts to only print elements 2-6 in list
print("Basic slice:", basic_slice)  # Prints [2, 3, 4, 5] 

# Slicing from the beginning (start not specified)
start_not_specified = my_list[:4]###Prompts to only print list before 4th element
print("Slice with start not specified:", start_not_specified)  # Prints [0, 1, 2, 3]

# Slicing until the end (end not specified)
end_not_specified = my_list[7:]###Prompts to only print list after 7th element
print("Slice with end not specified:", end_not_specified)  # Prints [7, 8, 9]

# Slicing with a step value
step_slice = my_list[1:8:2]###Prints every other number in list starting with first element
print("Slice with step value:", step_slice)  # Prints [1, 3, 5, 7]

# Slicing using negative indexes (relative to end of list)
negative_indexes = my_list[-5:-1]###Prompts to print relative to the end of the list (negative indicates that we're printing backwards)
print("Slice with negative indexes:", negative_indexes)  # Prints [6, 7, 8]
"""
"""
##Activity 6.Finding Items in Lists with the in Operator
# Sample list

my_list = [10, 20, 30, 40, 50]

# Check if an item is in the list using the 'in' operator
item_to_check = 30###Checks to make sure an element is in the list
if item_to_check in my_list:
    print(f"{item_to_check} is in the list.")###Prompts to inform user that given element is in list
else:
    print(f"{item_to_check} is not in the list.")###PPrompts to inform user that given item isn't in the list

# Check if an item is not in the list using the 'not in' operator
item_to_check = 60###Does the same thing as the previous lines
if item_to_check not in my_list:
    print(f"{item_to_check} is not in the list.")
else:
    print(f"{item_to_check} is in the list.")
"""
"""
##Activity 7. List Methods and Useful Built-in Functions (append, cont, index)
# Create an empty list


my_list = []

# Append items to the list using the append() method
my_list.append(10)###Adds new elements to the list
my_list.append(20)
my_list.append(30)
my_list.append(20)  # Adding the same item multiple times

# Count the number of times an item appears in the list using the count() method
item_to_count = 20###Prompts which item to count
count_result = my_list.count(item_to_count) ###Counts how many times element occurs in the list
print(f"The item {item_to_count} appears {count_result} times in the list.")###Prints how many times number appears

# Find the index of the first occurrence of an item using the index() method
item_to_find = 20###Gives item to find
try:
    index_result = my_list.index(item_to_find)###Tells when first occurance is
    print(f"The first occurrence of {item_to_find} is at index {index_result}.")
except ValueError:
    print(f"{item_to_find} is not in the list.")###Tells user that item isn't in the list

# Attempt to find the index of an item not in the list (raises ValueError)
item_not_in_list = 40###Locates item in list (Which isn't there)
try:
    index_result = my_list.index(item_not_in_list)
    print(f"The first occurrence of {item_not_in_list} is at index {index_result}.")###Tells user when item first occurs
except ValueError:
    print(f"{item_not_in_list} is not in the list, and it raises a ValueError.")###Tells user that item isn't found
"""
"""

####Activity 8. List Methods and Useful Built-in Functions (insert(), sort(), remove(), reverse(), del, sum(), min(), and max() )
# Create a list with some initial elements

my_list = [10, 30, 20, 40, 20]
print("initial list: ", my_list) ###Prints list
# Append items to the list using the append() method
my_list.append(50)
my_list.append(20)  # Adding 20 again
print("The list after appending elements 50 & 20: ", my_list)
# Insert an item at a specific index using the insert() method
my_list.insert(2, 25)###Inserts an element to replace in the index

# Sort the list using the sort() method (in-place)
my_list.sort()###Sorts list from least to greatest
print("print the list after sorting: ", my_list)
# Count the number of times an item appears in the list using the count() method
item_to_count = 20
count_result = my_list.count(item_to_count)###Tells how many of a specific element appears in list
print(f"The item {item_to_count} appears {count_result} times in the list.")

# Find the index of the first occurrence of an item using the index() method
item_to_find = 20
try:
    index_result = my_list.index(item_to_find)###Tells what ietm to find and when it firsy occurs in list
    print(f"The first occurrence of {item_to_find} is at index {index_result}.")
except ValueError:
    print(f"{item_to_find} is not in the list.")

# Remove an item from the list using the remove() method (removes the first occurrence)
item_to_remove = 20
my_list.remove(item_to_remove)###Removes item from list
print("print the list after removing 20: ", my_list)
# Reverse the list using the reverse() method (in-place)
my_list.reverse()###Reverses order (now from greatest to least)
print("print the list after reversing: ", my_list)
# Delete an item at a specific index using the del keyword
index_to_delete = 2
del my_list[index_to_delete]###deletes item from list
print("print the list after deleting item at index 2 ", my_list)
# Calculate the sum of the elements in the list using the sum() function
list_sum = sum(my_list)

# Find the minimum and maximum values in the list using the min() and max() functions
list_min = min(my_list) ###Finds minimum value in list
list_max = max(my_list)###Finds maximum value in list

# Print the updated list and the results of sum, min, and max
print("Updated list:", my_list)
print(f"Sum of elements: {list_sum}")
print(f"Minimum value: {list_min}")
print(f"Maximum value: {list_max}")
"""

"""
##Activity 9. Copying Lists
# Original list

original_list = [1, 2, 3, 4, 5]

# Method 1: Using a for loop to create a copy
copied_list1 = []###Copies original list
for item in original_list:
    copied_list1.append(item)

# Print the copied list
print("Method 1: Copied list using a for loop:", copied_list1)
# Original list
original_list = [1, 2, 3, 4, 5]

# Method 2: Concatenating the old list to create a copy
copied_list2 = [] + original_list

# Print the copied list
print("Method 2: Copied list using concatenation:", copied_list2)

# We can do some calculatuion on the list. Calculate the total of numeric values in the copied list
# Original list
original_list = [1, 2, 3, 4, 5]

# Create a copy of the original list
copied_list = list(original_list)

# Calculate the total of numeric values in the copied list
total = sum(item for item in copied_list) ###adds all elements in original list

# Calculate the average of numeric values in the copied list
average = total / len(copied_list) if copied_list else 0 ###Finds average of all elements in list

# Print the total and average
print("Total of numeric values in the copied list:", total)
print("Average of numeric values in the copied list:", average)


## Activity 10. Save a list to a file
# Function to save a list to a file

def save_list_to_file(file_name, input_list):
    with open(file_name, 'w') as file:
        file.writelines(f"{item}\n" for item in input_list)

# Function to read data from a file and return it as a list
def read_list_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]#line.strip() is a string method used to remove leading and trailing whitespace characters (such as spaces, tabs, and newline characters) from a string
    except FileNotFoundError:
        return []

# Original list
original_list = ['Apple', 'Banana', 'Cherry', 'Date']

# File name to save and read data
file_name = 'fruits.txt' ###Creates file and reads data from list

# Save the list to a file
save_list_to_file(file_name, original_list)###Saves file and adds from list

# Read data from the file
read_data = read_list_from_file(file_name) ###Reads from file

# Print the read data
print("Data read from the file:", read_data)


##Activity 11.List Comprehensions

list1 = [1, 2, 3, 4]
list2 = [item**2 for item in list1]###Prompts new list but squares all numbers
print ("previous list ", list1)
print ("new list ", list2)

##getting number of characters in string in list
str_list = ['Winken', 'Blinken', 'Nod']###Makes list from string
len_list = [len(s) for s in str_list]###makes original str list but makes all have 's' at the end
print("number of chars in each string in the list is: ", len_list)

### selctive items in list
list1 = [1, 12, 2, 20, 3, 15, 4]
list2 = []
for n in list1:###Prompts list to only enter values less than 10
    if n < 10:
        list2.append(n)
print ("list2 has all numbers that are less than 10:", list2)


### Activity 12. tTwo-dimensional list
# Create a two-dimensional list (3x3 matrix)

matrix = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] ###Creates matrix using integers

# Print the two-dimensional list
print("Two-dimensional list (matrix):")
for row in matrix:
    print(row)

# Accessing elements in the two-dimensional list
element_00 = matrix[0][0]  # Row 0, Column 0
element_12 = matrix[1][2]  # Row 1, Column 2 ###Finds values at given location in matrix
element_21 = matrix[2][1]  # Row 2, Column 1

print("\nAccessed elements:")
print(f"Element at [0][0]: {element_00}")
print(f"Element at [1][2]: {element_12}")
print(f"Element at [2][1]: {element_21}")

# Processing data in the two-dimensional list using nested loops
print("\nProcessed data:")
for row in matrix:
    for element in row:
        print(element, end=' ') #Each number is printed on the same line with spaces between them due to the end=' ' argument in the print() function.
    print()  # Print a newline after each row


## Activity 13. Tuples in Python
# Create a tuple with a list as its 3rd element

t = (10, 20, [97, 98, 99]) ###Creates tuple with embedded list, tuples cannopt be edited/changed

# Print the original tuple
print("Original tuple:", t)

# Access and modify the list within the tuple
mutable_list = t[2]###Prompts to edit list within tuple
mutable_list.append(100)  # Add an element to the list 

# Print the modified tuple
print("Modified tuple:", t)



## Activity 14. Covert Tuple to List and List to Tuple using
# Create a tuple with a list as its 3rd element

t = (10, 20, [97, 98, 99])

# Convert the tuple to a list using list()
list_from_tuple = list(t)

# Print the list obtained from the tuple
print("List from tuple:", list_from_tuple)

# Modify the list (now it's a list)
list_from_tuple[2].append(100)  # Add an element to the list

# Convert the modified list back to a tuple using tuple()
tuple_from_list = tuple(list_from_tuple)

# Print the final tuple
print("Tuple from modified list:", tuple_from_list)



"""
## Activity 15. Plotting Data with matplotlib

# This program displays a simple line graph.

import matplotlib.pyplot as plt

def main():
    # Create lists with the X and Y coordinates of each data point.
    x_coords = [0, 1, 2, 3, 4] ###Creates x and y coordinates for graph
    y_coords = [0, 3, 1, 5, 2]

    # Build the line graph.
    plt.plot(x_coords, y_coords) ###Plots points on graph

    # Display the line graph.
    plt.show() ###Prints graph

# Call the main function.
if __name__ == "__main__":
    main()

##Plotting a Bar chart
left_edges = [0, 10, 20, 30, 40] ###Makes dimensions for bars in bar graph
heights = [100, 200, 300, 400, 500] ###Prompts heights for bar graph

plt.bar(left_edges, heights)
plt.show()

## Plotting Pie cahart
values = [20, 60, 80, 40] ###Creates values in pie chart
plt.pie(values)
plt.show()
