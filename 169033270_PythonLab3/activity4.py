# Step 1: Declare two Boolean variables
bool_var1 = True
bool_var2 = False
# Step 2: Demonstrate logical operations (AND, OR, NOT)
# Logical AND
result_and = bool_var1 and bool_var2
print(result_and)
# Logical OR
result_or = bool_var1 or bool_var2
print(result_or)
# Logical NOT
result_not = bool_var1 and not bool_var2
print(result_not)
# Step 3: Use a Boolean variable in a conditional statement
if bool_var1 is True and bool_var2 is False:
    print("Conditions have been met")
else:
    print("Conditions have not been met")
# Conditional statement with logical operation
a = 15
b = 20

if a < b and b < 30:
    print("Both conditions are true, a is less than b and b is less than 30.")
elif a < b or b < 15:
    print("At least one of the conditions is true.")
else:
    print("No conditions are true.")
