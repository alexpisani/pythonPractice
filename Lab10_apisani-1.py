# Lab10_apisani-1.py
# Alex Pisani
# Aug 4 2024
# counts and lists alphabetically the frequency of each word from a given text file

import string

def printWds(data):
    """Print each word and its frequency, sorted alphabetically."""
    for word in sorted(data.keys()):
        print(f"{word}: {data[word]}")

def wordFreq(fptr):
    """Count the frequency of each word in the file pointed to by fptr."""
    freq = {}  # Initialize an empty dictionary for word frequency
    punctChars = tuple(string.punctuation)
    
    line = fptr.readline()  # Read the first line
    while line:
        # Remove punctuation characters
        for c in punctChars:
            line = line.replace(c, "")
        
        # Split the line into words
        words = line.split()
        
        for word in words:
            tmp = word.lower()  # Convert word to lowercase
            freq[tmp] = freq.get(tmp, 0) + 1  # Update the word count
        
        line = fptr.readline()  # Read the next line
    
    return freq

def main():
    filename = input("Enter the filename to read: ")
    
    try:
        with open(filename, 'r') as fptr:
            freq = wordFreq(fptr)
        
        printWds(freq)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

if __name__ == "__main__":
    main()