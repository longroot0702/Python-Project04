'''
- File Name: csv_function.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 28] File Version 1.0
'''

import usecsv

# Print Menu
def menu():
    print("----------[Make a file of foreigner ratio]----------\n")
    print("Please enter a standard of foreigner ratio(or more)")
    print("----------------------------------------------------")

# Make a file of foreigner ratio
def make_file(ratio):
    total = usecsv.opencsv('popSeoul.csv')
    newpop = usecsv.switch(total)

    new = [['Gu','Korean','Foreigner', 'Foreigner ratio(%)']]
    for i in newpop:
        foreign = 0
        try:
            foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
            if foreign > 3:
                new.append([i[0], i[1], i[2], foreign])
        except:
            pass

    usecsv.writecsv('newpop.csv', new)