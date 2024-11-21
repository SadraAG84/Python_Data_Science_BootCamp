import pandas as pd

data = pd.read_csv("../sources/weather_data.csv")
# ../sources/weather_data.csv
print(data)

# temp_list = data["temp"]
#
# avg = sum(temp_list) / len(temp_list)
# print(data["temp"].mean())
# print(avg)
#
# d_max = data["temp"].max()
#
# print(data[data["temp"] == d_max])
#
# monday = data[data["day"] == "Monday"]
# print(monday["temp"])