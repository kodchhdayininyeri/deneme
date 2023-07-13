from tkinter import *

window=Tk()
window.title("Mile to Km Converter")

window.config(padx=20,pady=20)


def miles_to_km():
    miles=float(entry_miles.get())
    km=miles*1.609
    kilometer_result.config(text=str(km))





entry_miles=Entry(width=7)
entry_miles.grid(column=1,row=0)

my_label=Label(text="Miles")
my_label.grid(column=2,row=0)

my_label2=Label(text="is equal to")
my_label2.grid(column=0,row=1)

kilometer_result=Label(text="0")
kilometer_result.grid(column=1,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(row=1,column=2)

calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=2,column=1)
print("hello")





window.mainloop()