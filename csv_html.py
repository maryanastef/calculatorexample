from prettytable import PrettyTable

csv_file = open('tests/test_data/data_csv.csv', 'r')
csv_file = csv_file.readlines()
print(csv_file)
line1 = csv_file[0]
line1 = line1.split(',')
line2 = csv_file[1]
line2 = line2.split(',')
print(line1, line2)

x= PrettyTable([line1[0], line2[0]])
for a in range(1,len(line1)):
    x.add_row([line1[a], line2[a]])
html_code = x.get_html_string()
html_file = open('tests/test_data/historical_table.html', 'w')
html_file = html_file.write(html_code)

