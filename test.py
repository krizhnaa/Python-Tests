# with open('./weather_data.csv') as file:
#     temp = file.readlines()
#     data = []
#     for _ in temp:
#         new_data = _.strip()
#         data.append(new_data)
#     print(data)

import csv

with open('./weather_data.csv') as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)