d1={
    "Bug":"An error",
    "Function":"A Feature",
    1:"number 1"
}

#Retrieving information
print(d1["Bug"])
print(d1[1])

#Adding items to it
d1["Loop"]="The action of doing something again and again"
print(d1)

#edit an item
d1["Bug"]="Moth in your Computer"
print(d1)

#accessing in for loop
for key in d1:
    print(key)
    print(d1[key])

#wipe off
d1={}
print(d1)

print("********************************************")

#Nesting Dictonary in Dicitionary
travel={"Pune":{"places_visited":["Shanivaar Wada","ABC Chowk"],"total_visits":15}}

#Nesting Dictionary in List (Urf JSON)
ghumna={
{
    "Place":"Pune",
    "foods":["WadaPaav","PaaniPuri","Lassi"],
    "total_visits":20,
},
{   "Place":"Pune",
    "garden":["BundGarden","OshoGarden"],
    "total_visits":40,
}
}
