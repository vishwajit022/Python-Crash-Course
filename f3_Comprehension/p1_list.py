range_list=[num*2 for num in range(1,5)]
print(range_list)

names=["Alex","Beth","Caroline","Ajay","Vishwajit"]

#Here we are returning the names where the length of names are less than 5
short_names=[_ for _ in names if len(_)<5]
print(short_names)
long_names=[n for n in names if len(n)>5]
print(long_names)

#Separating the even numbers from the list 
num=[23,21,33,12,54,12,43,54,67,80]
even=[n for n in num if n%2==0]
print(even)


#giving random scores to every student

names=["Vishwajit","Ajay","Kunal","Vijay"]
import random
student_scores={student:random.randint(0,100) for student in names}
print(student_scores)


