range_list=[num*2 for num in range(1,5)]
print(range_list)

names=["Alex","Beth","Caroline","Ajay","Vishwajit"]

#Here we are returning the names where the length of names are less than 5
short_names=[_ for _ in names if len(_)<5]
print(short_names)
long_names=[n for n in names if len(n)>5]
print(long_names)
