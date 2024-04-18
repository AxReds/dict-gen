# argparse: This module makes it easy to write user-friendly command-line interfaces.
import argparse

# itertools: This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
# Each has been recast in a form suitable for Python.
import itertools

# string: This module contains various string constant which contain the ASCII characters of all cases.
import string

def generate_combinations(min_length, max_length):
    """
    This function generates all possible combinations of characters within a specified length range.
    The characters used for combinations include lowercase letters, uppercase letters, digits, and symbols.
    The combinations are written to a file named 'combinations.txt'.
    """

    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all allowed characters
    allowed_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Generate combinations
    with open("combinations.txt", "w") as output_file:
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(allowed_characters, repeat=length):
                combination = "".join(combo)
                output_file.write(combination + "\n")

if __name__ == "__main__":
    """
    This is the main entry point of the script.
    It parses command line arguments for minimum and maximum length of combinations, and the filename to write to.
    Then it calls the function to generate combinations with the specified lengths and writes them to the specified file.
    """
    parser = argparse.ArgumentParser(description="Generate combinations of characters. This script generates all possible combinations of characters within a specified length range and writes them to a specified file.")
    parser.add_argument("--min-length", type=int, default=1, help="Minimum length of combinations")
    parser.add_argument("--max-length", type=int, default=5, help="Maximum length of combinations")
    parser.add_argument("--filename", type=str, default="combinations.txt", help="Filename to write combinations to")
    args = parser.parse_args()

    generate_combinations(args.min_length, args.max_length, args.filename)
    print(f"Combinations written to '{args.filename}'.")