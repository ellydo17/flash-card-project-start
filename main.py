from tkinter import *
import pandas
from pandas import DataFrame
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_2 ="#91C2AF"
WHITE = "#FFFFFF"
BLACK = "#000000"

# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
words_data = pandas.read_csv("./data/french_words.csv")
words_data_dict = words_data.to_dict(orient="records")
# print(words_data_dict)
current_word = {}

def random_word():
    global current_word, flip_duration
    window.after_cancel(flip_duration)
    current_word = random.choice(words_data_dict)
    word_label.config(text=current_word["French"], fg="black", bg=WHITE)
    language_label.config(text="French", fg="black", bg=WHITE)
    canvas.itemconfig(card_back_img_created, image=card_front_img)
    flip_duration = window.after(3000, flip_card)

# ---------------------------- FLIP THE CARDS ------------------------------- #
def flip_card():
    canvas.itemconfig(card_back_img_created, image=card_back_img)
    language_label.config(text="English", fg="white", bg=BACKGROUND_COLOR_2)
    word_label.config(text=current_word["English"], fg="white", bg=BACKGROUND_COLOR_2)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_duration = window.after(3000, flip_card) #defined here so that it is defined at the module level

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_front_img_created = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_back_img = PhotoImage(file="./images/card_back.png")
card_back_img_created = canvas.create_image(400, 263, image=card_back_img)

#Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=random_word)
right_button.grid(column=1, row=1)

#Texts
# canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"), fill="black")
# canvas.create_text(400, 263, text="Word", font=("Arial", 40, "bold"), fill="black")
language_label = Label(text="French", font=("Arial", 40, "italic"), fg=BLACK, bg=WHITE)
language_label.place(x=400, y=150, anchor="center")

word_label = Label(text="", font=("Arial", 40, "bold"), fg=BLACK, bg=WHITE)
word_label.place(x=400, y=263, anchor="center")
random_word()

window.mainloop()
