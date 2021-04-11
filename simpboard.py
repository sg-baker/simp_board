# Author: Samuel Baker
# Date Started: 2/19/2021
# Date Finished: 2/19/2021

from __future__ import print_function
#imports
# Person class
from simpboard_person import Person
#Bubble sort
from simpboard_person import person_bubble_sort
# Data visualization
from simpboard_graphing import barplot
# Google Sheets API and Authorization
import gspread
# Data framing
import pandas as pd
import json



# CONSTANTS
SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = r"C:\\Users\samue\\OneDrive\Desktop\Simp_Board\simp-board-python-api-dc14d963eea5.json"
SPREADSHEET = "SIMP BOARD Coaches Poll April '21 (Responses)"
# Have to change the name of the spread sheet if using a new spreadsheet

# Authentication with google sheets and gspread
gc = gspread.service_account(filename=SECRETS_FILE)

"""
print("These are all of the sheets:")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))
"""
# Gets all sheets onto one workbook
wrkbook = gc.open(SPREADSHEET)
# Get the first sheet
sh = wrkbook.sheet1
# Read sheet into a data frame using pandas
data = pd.DataFrame(sh.get_all_records())

# Getting names into a list
columns = list(data)
# Creating final ranking liat
rank = []

# Iterating over each name
# and adding it to the list
for col in columns[2::]:
    sum = 0
    for row in range(len(sh.col_values(1)) - 1):
        # Finding aggregate
        sum += int(data[col][row])
    # Creation of person and appending list
    per = Person(col, sum)
    rank.append(per)

# Sorting, there will always be 25 people
person_bubble_sort(rank, 25)
# Lists used for data visualization
names =[]
agg = []
for i in rank:
    names.append(i.name)
    agg.append(i.aggregate)

# Bar plot creation
barplot(names, agg, "Brother in Question", "Total Simpage", "SIMP BOARD")