from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 30*60
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_command():
    window.after_cancel(timer)
    global rep
    rep = 0
    timer_label.config(text='Timer')
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_command():
    global rep
    rep += 1

    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Long break", fg=RED)

    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Short break", fg=PINK)

    else:
        count_down(WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_command()
        mark = int(rep/2)
        check_mark.config(text=f"{'✓'*mark}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Naru's pomodor")
window.config(padx=150, pady=50, bg=YELLOW)


timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

start_button = Button(text='start', command=start_command, font=(FONT_NAME,10,'bold'), highlightthickness=0)
start_button.grid(column=0, row=3)

reset_button = Button(text='reset', command=reset_command, font=(FONT_NAME,10,'bold'), highlightthickness=0)
reset_button.grid(column=3, row=3)

check_mark = Label(font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=3)

canvas = Canvas(width=400, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 120, image=tomato_img)

timer_text = canvas.create_text(200, 140, text="00:00", fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=2, row=2)






window.mainloop()
