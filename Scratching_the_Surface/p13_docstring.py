def fullname(f,l):
    """Set title format for"""
    newf=f.title()
    newl=l.title()
    return newf,newl

print(fullname(input("What is your FirstName?"),input("What is your Last Name?")))

fullname()
#If we hover over this it will show the docstring