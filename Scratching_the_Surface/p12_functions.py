def fullname(f,l):
    newf=f.title()
    newl=l.title()
    return newf,newl

print(fullname(input("What is your FirstName?"),input("What is your Last Name?")))