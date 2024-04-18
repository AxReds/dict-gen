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
import itertools # itertools: This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
import string # string: This module contains various string constant which contain the ASCII characters of all cases.
import sys # sys: This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import json # json: This module implements a subset of JavaScript Object Notation (JSON) as a data interchange format.
import os # os: This module provides a way of using operating system dependent functionality.
import threading # threading: This module constructs higher-level threading interfaces on top of the lower level thread module.
import signal # signal: This module provides mechanisms to use signal handlers in Python.
import time # time: This module provides various time-related functions.

#Global variables
global min_length, max_length, combination, id_combinations, id_iterations

# Function to perform countdown
def countdown(seconds):
    while seconds > 0:
        print(f"Countdown: {seconds} seconds remaining...")
        time.sleep(1)
        seconds -= 1

# Function to get user confirmation to continue from the last checkpoint
def get_confirmation(min_length, max_length, last_combination):
    return input(f"Do you want to continue from the last checkpoint? (min-length: {min_length}, max-length: {max_length}, last combination: {last_combination}) (y/n) ")

# Function to handle SIGINT signal
def handle_sigint(signum, frame):
    write_checkpoint(min_length, max_length, combination, id_combinations, id_iterations)
    print("\nUser interruption detected. Current state saved to checkpoint file.")
    sys.exit(1)

# Function to load the checkpoint file if it exists
def load_checkpoint():
    checkpoint_file = "checkpoint.json"
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, "r") as f:
            checkpoint = json.load(f)
            min_length = checkpoint['min_length']
            max_length = checkpoint['max_length']
            last_combination = checkpoint['last_combination']
            id_combinations = checkpoint['id_combinations']
            id_iterations = checkpoint['id_iterations']

        # Start a timer for user confirmation
        timer = threading.Timer(10.0, lambda: print("\nTime's up! Restarting from scratch..."))
        timer.start()
        countdown_thread = threading.Thread(target=countdown, args=(10,))
        countdown_thread.start()
        confirmation = get_confirmation(min_length, max_length, last_combination)
        timer.cancel()
        countdown_thread.join()

        # If user does not confirm, reset to default values
        if confirmation.lower() != 'y':
            min_length = default_min_length
            max_length = default_max_length
            id_combinations = 0
            id_iterations = 0
            last_combination = ""
    else:
        # If checkpoint file does not exist, use default values
        min_length = default_min_length
        max_length = default_max_length
        id_combinations = 0
        id_iterations = 0
        last_combination = ""

    return min_length, max_length, id_combinations, id_iterations, last_combination

# Function to write the current state to the checkpoint file
def write_checkpoint(min_length, max_length, last_combination, id_combinations, id_iterations):
    checkpoint_file = "checkpoint.json"
    with open(checkpoint_file, "w") as f:
        checkpoint = {'min_length': min_length, 'max_length': max_length, 'last_combination': last_combination, 'id_combinations': id_combinations, 'id_iterations': id_iterations}
        json.dump(checkpoint, f)


# Function to generate all possible combinations of characters within a specified length range
def generate_combinations(min_length, max_length, filename):
    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    #tofix
    last_combinations = ""

    # Combine all allowed characters
    allowed_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Load the checkpoint file
    min_length, max_length, id_combinations, id_iterations, last_combinations = load_checkpoint()

    # Set the signal handler
    signal.signal(signal.SIGINT, handle_sigint)

    # Generate combinations
    with open(filename, "w") as output_file:
        for length in range(min_length, max_length + 1):
            id_iterations += 1
            for combo in itertools.product(allowed_characters, repeat=length):
                id_combinations += 1
                combination = "".join(combo)
                output_file.write(combination + "\n")
                print(str(id_iterations) +"/"+ str(id_combinations) + " - Combination: " + combination)
                # Save the current state to the checkpoint file every combination
                write_checkpoint(min_length, max_length, combination, id_combinations, id_iterations)


#
#This is the main entry point of the script.
#It parses command line arguments for minimum and maximum length of combinations, and the filename to write to.
#Then it calls the function to generate combinations with the specified lengths and writes them to the specified file.    
if __name__ == "__main__":

    # Set default values for minimum length, maximum length, and filename
    default_min_length = 1
    default_max_length = 5
    default_filename = "combinations.txt"
    
    # Set a default description for the script
    default_description = "AxReds' Dictionary Generator generates combinations of characters.\n" \
                          "This script generates all possible combinations of characters within a specified length range and writes them to a specified file."

    # Initialize argument parser with the default description
    parser = argparse.ArgumentParser(description=default_description)
    
    # Add arguments for minimum length, maximum length, and filename with their default values and help texts
    parser.add_argument("--min-length", type=int, default=default_min_length, help="Minimum length of combinations")
    parser.add_argument("--max-length", type=int, default=default_max_length, help="Maximum length of combinations")
    parser.add_argument("--filename", type=str, default=default_filename, help="Filename to write combinations to")
    
    # Parse the arguments
    args = parser.parse_args()

    # Print the default description
    print(default_description)
    
    # If no arguments were provided, ask the user for input
    if len(sys.argv) == 1:
        args.min_length = int(input(f"Enter minimum length of combinations (default is {default_min_length}): ") or default_min_length)
        args.max_length = int(input(f"Enter maximum length of combinations (default is {default_max_length}): ") or default_max_length)
        args.filename = input(f"Enter filename to write combinations to (default is '{default_filename}'): ") or default_filename
   
    # Call the function to generate combinations with the specified lengths and write them to the specified file
    generate_combinations(args.min_length, args.max_length, args.filename)
    
    # Print a message indicating that the combinations have been written to the file
    print(f"Combinations written to '{args.filename}'.")