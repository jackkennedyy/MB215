##Python Program for Demonstrating Different Uses of for Loops

# For loop with range to print even numbers from 2 to 20
count = 2
while count <= 20:
    print ("Count is", count)
    count += 2

# Nested for loop to create a multiplication table for numbers 1 to 3

for x in range (1, 4): 
    for y in range (1, 4):
        result = x * y
        print (f"[{x} * {y} = {result}")

# For loop to reverse a string. Note : Use ‘Reserved’ Key word

word = "hello"
reversedword = ''.join(reversed(word))
print(reversedword)
