import csv

with open('weather.csv','r') as file:
    data = list(csv.reader(file))

print(data)

city = input('Enter city: ')

for row in data[1:]:
    if city == row[0]:
        print(f'Temperature is {row[1]}')