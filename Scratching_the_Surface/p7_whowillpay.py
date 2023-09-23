import random

people = input("Names of the members who went for lunch, separated by comma: ")
names_list = people.split(", ")
x=len(names_list)-1
print(x)

if not names_list:
    print("No names entered. Please enter at least one name.")
else:
    chosen = random.choice(0,)
    print(f"The randomly chosen person for lunch is: {chosen}")
    
