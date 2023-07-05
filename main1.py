from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
languages = ["Danish", "English"]


data = pandas.read_csv("Cartella 3.csv")
to_learn = data.to_dict(orient="records")


def next_card(checked):
    global current_card


    unknown_button["state"] = "normal"
    known_button["state"] = "normal"

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Danish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Danish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    if checked:
        is_known()





def flip_card(checked):
    print("inizio")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    print("end")

    window.after(3000, func=lambda: next_card(checked))

    print("dopo sleep")


def is_known():

    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Cartella 3.csv", index=False)
    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Congratulations")
        canvas.itemconfig(card_word, text="you've learned 1000 words!!", font=("Ariel", 40, "italic"))


def check_answer(checked=False):
    unknown_button["state"] = "disabled"
    known_button["state"] = "disable"
    print("prima di flip")
    flip_card(checked)
    print("dopo di flip")



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)

#option_var = StringVar()
#option_var.set("Select language")
#menu_tendina = OptionMenu(window, option_var, *languages)
#menu_tendina.grid(row=0, column=1)
#option_var.trace("w", next_card)


card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=check_answer)
unknown_button.grid(row=1, column=0)


check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, highlightthickness=0, command=lambda: check_answer(True))
known_button.grid(row=1, column=1)




next_card(False)

window.mainloop()



