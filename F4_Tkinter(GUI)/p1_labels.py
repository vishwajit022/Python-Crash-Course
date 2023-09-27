import tkinter
window=tkinter.Tk()

window.title="THis is My GUI Program"
window.minsize(width=500,height=300)

#label
my_lable=tkinter.Label(text="I am a label" ,font=("Arial",20,"italic","bold"))
my_lable.pack()
#Shifts to left
my_lable.pack(side="left")

my_lable2=tkinter.Label(text="I am a label" ,font=("Arial",20,"italic","bold"))
my_lable2.pack(side="bottom")

#This should be always at the end of the program
window.mainloop()