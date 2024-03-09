"""
1. create a program letting user to have 2 CLA
2. the name of an existing CSV as input, column are assume to be 'name and house'
3. create a new CSV to write as output, shoule have 3 columns 'first, last and house'
4. convert input into that output, split name into first name and last name, assume each student would have first and last name

Corner-case
1. don't have 2 CLA
2. first one cant be read
-> should sys.exit

"""

import csv
import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            format_list = convert_format(sys.argv[1])
            header = ["first", "last", "house"]
            convert_csv("after.csv", format_list, header)
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

def convert_format(sample_csv):
    after = []
    with open(sample_csv, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
                first, last = row["name"].split(", ")
                after.append({"first": first, "last": last, "house": row["house"]})
    return after

def convert_csv(new_table_name, format_table, header):
     with open(new_table_name, "w", newline= "") as file:
          writer = csv.DictWriter(file, fieldnames= header)
          writer.writeheader()
          writer.writerows(format_table)

    # importing pandas of donig it 
#           df = pd.DataFrame(people)
# df.to_csv('people.csv', index=False, header=['first', 'last', 'house'])


if __name__ == "__main__":
     main()
