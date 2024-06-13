# PASSWORD GENERATOR

import random
import string

def generate_password(length):
    # Define the possible characters to include in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters from the possible set
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user to specify the desired length of the password
    length = input("Enter the desired length for the password: ")
    
    # Check if the input is a positive integer
    if length.isdigit():
        length = int(length)
        if length > 0:
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print(f"Generated password: {password}")
        else:
            print("Please enter a positive integer.")
    else:
        print("Invalid input. Please enter a valid number.")


main()
