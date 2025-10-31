# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

# Author: Zepora Lilly
# Date: 10/31/2025
def count_file_lines():
    ######################
    # Add your code here #
    ######################
    try:
        with open("names.txt","r") as file:
            lines = file.readlines()
            print("Number of names in the file:", len(lines))
    except FileNotFoundError:
        print("error: 'names.txt' not found.")

    print('In the count_file_lines function')
# Run the program




# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()