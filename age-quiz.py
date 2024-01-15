# Print what this program does
print("Where are you in your life? Enter your age to find out.")

# This function validates the users input
def get_valid_integer(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_input = int(user_input)  # Try to convert input to an integer

            # Validation: Ensure the input meets additional criteria
            if user_input < 0:
                print("Please enter a non-negative integer.")
            else:
                return user_input  # Return valid input if all conditions are met

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# User enters their age to run the code:
age = get_valid_integer("Enter your age: ")
print("You entered:", age)

# Run program based on entered age:
if age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
else:
    print("Age is but a number.")