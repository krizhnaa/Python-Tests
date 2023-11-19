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

# import pandas
#
# data_dict = {
#     'students' : ['Amy', 'James', 'Vichu'],
#     'scores' : [10, 12, 15]
# }
#
# data = pandas.DataFrame(data_dict)
# # print(data)
#
# data.to_csv('data_csv')

import pandas as py

data = py.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_color_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_color_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_color_count = len(data[data['Primary Fur Color'] == 'Black'])


data_dict = {
    'Fur' : ['grey', 'red', 'black'],
    'Count' : [gray_color_count, red_color_count, black_color_count]
}

df_data = py.DataFrame(data_dict)

df_data.to_csv('csv_data')







