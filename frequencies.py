"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    #items is a list
    for i in range(len(items)):
        count = 0
        items[i] = str(items[i])

        for j in range(len(items)):  
            if items[i] == items [j]:
                count += 1 
            frequencies[items[i]] = count   
              
    return frequencies
