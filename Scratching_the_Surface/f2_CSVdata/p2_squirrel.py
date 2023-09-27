import pandas
data = pandas.read_csv("squirrel.csv", encoding="utf-8")
grey=len(data[data["Primary Fur Color"]=="Gray"])
print(grey)
red=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(red)
black=len(data[data["Primary Fur Color"]=="Black"])
print(black)

data_dict={
    "Squirrels":["Gray","Cinnamon","Black"],
    "Count:":[grey,red,black],
}
export=pandas.DataFrame(data_dict)
export.to_csv("exportsquireel.csv")