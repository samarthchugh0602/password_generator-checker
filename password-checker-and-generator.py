import random
import string

def generate_password():
    """Generates a strong random password with at least one lowercase,
    uppercase, digit, and special character, with a random length between 8 and 12."""
    
    
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digit_chars = string.digits
    special_chars = string.punctuation
    
    
    all_characters = lower_chars + upper_chars + digit_chars + special_chars
    
    
    length = random.randint(8, 12)
    print(f"\nGenerating a password of length: {length}")
    
    
    min_chars_for_guarantee = 4 

    
    password_characters = []
    password_characters.append(random.choice(lower_chars))
    password_characters.append(random.choice(upper_chars))
    password_characters.append(random.choice(digit_chars))
    password_characters.append(random.choice(special_chars))

    
    remaining_length = length - min_chars_for_guarantee
    for _ in range(remaining_length):
        password_characters.append(random.choice(all_characters))

    
    random.shuffle(password_characters)

   
    password = ''.join(password_characters)
    print(f"Generated Password: {password}")

def check_password_strength():
    """Checks the strength of a password based on presence of char types and length."""
    
    password = input("Enter the password to check: ")
    length = len(password)
    
   
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

   
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation: 
            has_special = True
    
    
    num_types = 0
    if has_lower: num_types += 1
    if has_upper: num_types += 1
    if has_digit: num_types += 1
    if has_special: num_types += 1
        
    print(f"\nPassword: {password}")
    print(f"Length: {length} characters")
    print("Contains:")
    print(f"  - Lowercase: {'Yes' if has_lower else 'No'}")
    print(f"  - Uppercase: {'Yes' if has_upper else 'No'}")
    print(f"  - Digits:    {'Yes' if has_digit else 'No'}")
    print(f"  - Special:   {'Yes' if has_special else 'No'}")
    print(f"  - Unique character types: {num_types}/4") 

    
    strength_rating = ""

    if length < 8:
        strength_rating = "Very Weak (Too short - aim for at least 8 characters)"
    elif length < 12:
        if num_types < 3:
            strength_rating = "Weak (Good length, but needs more character types)"
        elif num_types == 3:
            strength_rating = "Medium (Good length and variety, almost strong!)"
        else: 
            strength_rating = "Strong (Excellent! All types present at a good length)"
    else: 
        if num_types < 3:
            strength_rating = "Medium (Great length, but could use more character variety)"
        elif num_types == 3:
            strength_rating = "Strong (Excellent! Great length and good variety)"
        else: 
            strength_rating = "Very Strong (Outstanding! Long and highly diverse)"

    print(f"Strength: {strength_rating}")
    

def main():
    """Main function to run the password tool."""
    print("--- Password Tool ---")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Generate Password")
        print("2. Check password strength")
        print("0. Exit")
        
        user_demand = input("Type 1, 2, or 0: ").strip()

        if user_demand == '1':
            generate_password()
        elif user_demand == '2':
            check_password_strength()
        elif user_demand == '0':
            print("Exiting Password Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please type 1, 2, or 0.")

if __name__ == "__main__":
    main()
