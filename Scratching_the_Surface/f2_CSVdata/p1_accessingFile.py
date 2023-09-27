import pandas
data=pandas.read_csv("weather_data.csv")
#print(data["condition"])
#print(data["temp"])

templist=data["temp"].to_list()
#print(templist)

average=sum(templist)/len(templist)
#print(average)
#OR
print(data["temp"].mean())
print(data["temp"].max())

#to return a particular row
print(data[data.temp==24])

print(data[data.temp==data.temp.max()])


#Create a data frame from Scratch
data_dict={
    "students":["Amy","Jamy","Julie"],
    "scores":[23,43,41],
}
data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")