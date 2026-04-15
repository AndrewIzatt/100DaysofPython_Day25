import csv
with open("./weather_data.csv", mode="r") as data_file:
    # data = data_file.readlines()
    # print(data)
    data = csv.reader(data_file)
    # print(data)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temp_int = int(row[1])
            temperatures.append(temp_int)
        # print(temp_int)
    print(temperatures)