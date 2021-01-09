#importing file and module
import csv
import os

import_budget_data = os.path.join("Resources", "budget_data.csv")

#reading in the header
with open(import_budget_data) as budget_data:
    read_csv = csv.reader(budget_data)

    header = next(read_csv)
