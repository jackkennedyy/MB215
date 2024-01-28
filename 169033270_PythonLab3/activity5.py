total = 0 ###creates variables for total number and count
count = 0

while total < 100: ### creates conditional loop that breaks when convenient for user
    user_input = input("Enter your value: ")
    if user_input == " ":
        break
    num = float(user_input)
    total += num
    count += 1

print("Your total:", total) ### prints total sum and amount of numbers used
print("Amount of numbers entered:", count)
