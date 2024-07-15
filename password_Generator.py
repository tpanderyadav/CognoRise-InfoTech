import random
import string 
def generate_password(length=10):
    # Define the character sets to use in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    
    # Combine all the characters
    all_characters = lowercase_letters + uppercase_letters + digits
   
    # Use random.sample to generate a list of random characters and then join them
    password = ''.join(random.sample(all_characters, length))
    return password
password = generate_password()
print("Generated Password:",password)