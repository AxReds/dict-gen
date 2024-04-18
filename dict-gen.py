#AxReds' Dictionary Generator - v1.0.
#Copyright (C) 2020 Alessio Rossini <alessior@live.com>
#Original source code available at https://github.com/AxReds/dict-gen
#
#Description:
#This script generates all possible combinations of characters within a specified length range and writes them to a specified file.
#
#Licensing:
#This program is free software; you can redistribute it and/or modify it under
#the terms of the GNU General Public License as published by the Free Software Foundation;
#either version 2 of the License, or any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#See the GNU General Public License for more details
#https://opensource.org/
#
#You should have received a copy of the GNU General Public License along with this program; 
#if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
#

#Include libraries
import argparse # argparse: This module makes it easy to write user-friendly command-line interfaces.
import string # string: This module contains various string constant which contain the ASCII characters of all cases.
# itertools: This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
# Each has been recast in a form suitable for Python.
import itertools

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
    parser = argparse.ArgumentParser(description="AxReds' Dictionary Generator. Generate combinations of characters. This script generates all possible combinations of characters within a specified length range and writes them to a specified file.")
    parser.add_argument("--min-length", type=int, default=1, help="Minimum length of combinations")
    parser.add_argument("--max-length", type=int, default=5, help="Maximum length of combinations")
    parser.add_argument("--filename", type=str, default="combinations.txt", help="Filename to write combinations to")
    args = parser.parse_args()

    generate_combinations(args.min_length, args.max_length, args.filename)
    print(f"Combinations written to '{args.filename}'.")