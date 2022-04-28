'''
- File Name: main.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 28] File Version 1.0
'''

import csv_function

ratio = 0

csv_function.menu()

while True:

    try:
        ratio = int(input("\nstandard of foreigner ratio(%): "))
    except ValueError:
        print("\nError: Illegal Value..")
    else:
        break

csv_function.make_file(ratio)
print("\nCSV file was successfully created!")
