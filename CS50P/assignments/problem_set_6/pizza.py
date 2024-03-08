"""
1. create a program that expects have exact one CLA, refer to the pizza price table
2. formulate the table using 'tabulate', a package of PyPI, format the table using 'grid'

# Handle corner case
- does not specify exact one CLA
- does not specify file name as ".py"
- does not have CLA
-> should print sys.exit

"""
from tabulate import tabulate
import sys
import csv

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not(sys.argv[1].endswith(".csv")):
            sys.exit("Not a CSV file")
        else:
            print(print_table(sys.argv[1]))

    except FileNotFoundError:
        sys.exit("File does not exist")

def print_table(table):
    with open(table) as file:
        reader = csv.reader(file)
        format_table = tabulate(reader, tablefmt="grid")

    return format_table

if __name__ == "__main__":
    main()