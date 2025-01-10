import csv
from tabulate import tabulate
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    
headers=["NAME", "Age", "City"]
with open('output.csv', mode='r',encoding="utf-8", newline='') as file:
    csv_reader = csv.DictReader(file)
    liste=  [x for x in csv_reader]
    print(tabulate(liste, headers="", tablefmt="grid"))
