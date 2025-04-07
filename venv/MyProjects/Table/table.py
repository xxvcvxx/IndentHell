import csv

from prettytable import PrettyTable
table = PrettyTable()

with open("toDo.txt",newline='') as fp:

    reader = csv.reader(fp, delimiter=',')
    headers = next(reader)
    table.field_names = headers

    for row in reader:
        table.add_row(row)

print(table)
