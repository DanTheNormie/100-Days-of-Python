import tkinter

window = tkinter.Tk()
window.title("Danny's GUI")
window.minsize(500, 300)

# Labels

label_1 = tkinter.Label(text="This is a Text_View")
label_1.pack()

label_1["text"] = "New Text"
label_1.config(text="New Text")

# Buttons

btn_click_counter = 0


def btn_on_click():
    global btn_click_counter
    btn_click_counter += 1
    label_1["text"] = f"Button Click {btn_click_counter}"
    label_1.config(text=input.get())


button_1 = tkinter.Button(text="Click Me", command=btn_on_click)
button_1.pack()

# Entry

input = tkinter.Entry(width=10)
input.insert(tkinter.END, "")
input.pack()

tkinter.mainloop()
