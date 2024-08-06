import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())
print(data["temp"].max())

print(sum(temp_list) / len(temp_list))

total = 0
for item in temp_list:
    total += item
print(total / len(temp_list))

max_temp = data["temp"].max()
print(data[data.temp == max_temp])

print(data["condition"])

print(data.condition)

print(data[data.temp == data.temp.max()])

print([data.day == "Monday"])
