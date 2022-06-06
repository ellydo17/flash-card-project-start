from tkinter import *
import pandas
from pandas import DataFrame
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"

# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
words_data = pandas.read_csv("./data/french_words.csv")
data_frame = pandas.DataFrame(words_data)
words_data_dict = data_frame.to_dict(orient="records")
# print(type(words_data_dict))

def random_word():
    english_word = random.choice(words_data_dict)
    word_label.config(text=english_word["English"])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

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
language_label = Label(text="English", font=("Arial", 40, "italic"), fg=BLACK, bg=WHITE)
language_label.place(x=400, y=150, anchor="center")

word_label = Label(text="English", font=("Arial", 40, "bold"), fg=BLACK, bg=WHITE)
word_label.place(x=400, y=263, anchor="center")

window.mainloop()