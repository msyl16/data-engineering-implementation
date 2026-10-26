import sys

import pandas as pd

# Using command line arguments

if len(sys.argv) < 3: 
    print("Usage: python script.py <number1> <number2>") 
    sys.exit(1)

script_name = sys.argv[0]
number1 = sys.argv[1]
number2 = sys.argv[2]

print("Script Name: ", script_name)
print("Version 1: ", number1)
print("Version 2: ", number2)

