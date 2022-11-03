from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#E97777"
BROWN = "#9E7676"
BLUE = "#b9e0ff"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE = 30
FONT_STYLE = "bold"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
rep_counter = 0
timer = None
timer_running = False

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("POMODORO")

# canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"), tags="timer")
canvas.grid(row=2, column=2)

# title
title = Label(text="{: ^14}".format(" Timer"), font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN, bg=YELLOW)
title.grid(row=1, column=2)


# button functions
def start_cmd():
    if not timer_running:
        global rep_counter
        match rep_counter:

            case 8:
                time = LONG_BREAK_SEC
                title.config(text="{: ^13}".format(" Long Break 🍵"), font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=BROWN)
                rep_counter = 0

            case rep_counter if not rep_counter % 2 == 0:
                time = SHORT_BREAK_SEC
                title.config(text="{: ^13}".format("Short Break 🐳"), font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)

            case rep_counter if rep_counter % 2 == 0:
                time = WORK_SEC
                title.config(text="{: ^15}".format("Work 👨‍💻"), font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=RED)

        update_timer(time)
        rep_counter += 1


def reset_cmd():
    global rep_counter, timer, timer_running
    if timer is not None:
        window.after_cancel(timer)
        timer_running = False
        rep_counter = 0
        title.config(text="{: ^14}".format("Timer"), font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
        counter.config(text="")
        canvas.itemconfig(timer_txt, text="00:00")


# buttons
start_btn = Button(text="Start", command=start_cmd)
start_btn.grid(row=3, column=1)
reset_btn = Button(text="Reset", command=reset_cmd)
reset_btn.grid(row=3, column=3)

# pomodoro counter
counter = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
counter.grid(row=4, column=2)


def update_timer(time):
    global timer_running, timer
    if time > -1:
        timer_running = True
        time_min = int(time / 60)
        time_sec = time % 60

        canvas.itemconfig(timer_txt, text=f"{time_min:02}:{time_sec:02}")

        timer = window.after(1, update_timer, time - 1)
    else:
        timer_running = False
        counter.config(text="{0:✔^{1}}".format("", int(rep_counter / 2)))
        start_cmd()


window.mainloop()
