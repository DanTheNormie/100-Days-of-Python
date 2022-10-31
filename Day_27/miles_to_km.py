import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Miles to Kilo-meters Converter")

entry = Entry()
entry.grid(column=2, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=3, row=1)

label_isequalto = Label(text="is equal to")
label_isequalto.grid(column=1, row=2)

label_result = Label(text="0")
label_result.grid(column=2, row=2)

label_km = Label(text="Km")
label_km.grid(column=3, row=2)


def convert_miles_to_km():
    miles = int(entry.get())
    km = miles * 1.609
    label_result.config(text=f"{km}")


calc_button = Button(text="Calculate", command=convert_miles_to_km)
calc_button.grid(column=2, row=3)

window.mainloop()
