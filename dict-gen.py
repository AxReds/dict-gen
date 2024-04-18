import argparse
import itertools
import string

def generate_combinations(min_length, max_length):
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

if _name_ == "_main_":
    parser = argparse.ArgumentParser(description="Generate combinations of characters.")
    parser.add_argument("--min-length", type=int, default=1, help="Minimum length of combinations")
    parser.add_argument("--max-length", type=int, default=5, help="Maximum length of combinations")
    args = parser.parse_args()

    generate_combinations(args.min_length, args.max_length)
    print(f"Combinations written to 'combinations.txt'.")
