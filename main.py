from tkinter import *
import pandas as pd
import random

from pandas.errors import EmptyDataError

from constants import constants
current_card = {}
words_learned = {}

try:
    word_data = pd.read_csv('language_data/words_to_learn.csv')
except EmptyDataError:
    starting_data = pd.read_csv('language_data/french_words.csv')
    to_learn = starting_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")

def get_card_vocab():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous flip timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_face, image=card_front_image)
    flip_timer = window.after(3000, flip_card) # Reset the flip timer for the new card

def flip_card():
    canvas.itemconfig(title_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_face, image=card_back_image)

def words_to_learn():
    try:
        to_learn.remove(current_card)  # Remove the known word from the list
        words_to_review = pd.DataFrame(to_learn)
        words_to_review.to_csv('language_data/words_to_learn.csv', index=False)  # Save the updated list
    except IndexError:
        canvas.itemconfig(title_language, text="No more words to learn!", fill="red")
    else:
        get_card_vocab()  # Get a new card vocabulary

window = Tk()
window.title(constants.WINDOW_TITLE)
window.config(padx=50, pady=50, bg=constants.BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card) # Initial flip timer starts right when program runs

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_face = canvas.create_image(400, 263, image=card_front_image)
title_language = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")
canvas.config(bg=constants.BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_word_button_image = PhotoImage(file="images/wrong.png")
unknown_word_button = Button(image=unknown_word_button_image, command=get_card_vocab ,highlightthickness=0)
known_word_button_image = PhotoImage(file="images/right.png")
known_word_button = Button(image=known_word_button_image, command=words_to_learn ,highlightthickness=0)

unknown_word_button.grid(row=1, column=0)
known_word_button.grid(row=1, column=1)

get_card_vocab()

# must be at the bottom of the file
window.mainloop()