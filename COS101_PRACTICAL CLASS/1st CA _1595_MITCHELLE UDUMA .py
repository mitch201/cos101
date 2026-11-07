while True:
    # Ask the user for a number or an option to exit
    user_input = input("Enter a number (or type 'end' to quit): ")
    
    # Check if the user wants to exit the program
    if user_input.lower() == "end":
        print("Exiting the program. Goodbye!")
        break
    
    try:
        # Convert the input to an integer
        number = int(user_input)
        
        # Check if the number is less than 1
        if number < 1:
            print("Invalid input! Please enter a number greater than or equal to 1.\n")
            continue  # Restarts the loop to ask for input again
        
        # Generate and display the multiplication table if the number is valid
        print(f"\n--- Multiplication Table for {number} ---")
        for multiplier in range(1, 13):
            product = number * multiplier
            print(f"{number} x {multiplier} = {product}")
        print() # Adds an empty line for neat formatting
        
    except ValueError:
        # Handles cases where the user types random letters instead of a number
        print("That's not a valid number. Please try again.\n")

