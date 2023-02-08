from prettytable import PrettyTable

th = ['test', 'name', 'case', 'cycle']
td = [1, 2, 3, 4, 5, 6, 7, 8]

columns = len(th)
table = PrettyTable(th)
td_data = td[:]
while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]

print(table)
