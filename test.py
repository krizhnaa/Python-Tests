# with open('./weather_data.csv') as file:
#     temp = file.readlines()
#     data = []
#     for _ in temp:
#         new_data = _.strip()
#         data.append(new_data)
#     print(data)

# import csv
#
# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     temperature = []
#     for row in data:
#         temp.append(row[1])
#     for dats in temp[1:]:
#         temperature.append(int(dats))
#     print(temperature)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# fahren = ( monday_temp * 9/5 ) + 32
# print(fahren)

import pandas

data_dict = {
    'students' : ['Amy', 'James', 'Vichu'],
    'scores' : [10, 12, 15]
}

data = pandas.DataFrame(data_dict)
# print(data)

data.to_csv('data_csv')







