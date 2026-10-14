def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: 3 and then 4 because it adds 1 if the number is greater than 1. Only 2 and 3 are greater than 1.  

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: It would return 3 because 2 takes the position of the value that 1 is being added to. Return inside the function sets up what you want to be produced? Print in the loop prints the numbeer on the screen using the defintion. 
