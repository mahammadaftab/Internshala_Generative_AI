# 1. Print greeting message
print("Hello, World!")

# 2. Take two numbers from user and print their sum
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
print("The sum is:", sum_result)

# 3. Define variables and perform arithmetic
my_string = "Artificial Intelligence"
my_number = 10

result = my_number + 5
print("The result of adding 5 to", my_number, "is:", result)

# 4. Comments are added throughout the code (as you can see)

# 5. Take string input from user
user_text = input("Please enter a string: ")
print("You entered:", user_text)

# 6. Check if number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 7. While loop to ensure positive number
while True:
    positive_num = float(input("Enter a positive number: "))
    
    if positive_num > 0:
        print("You entered:", positive_num)
        break
    else:
        print("Invalid input. Please enter a positive number.")