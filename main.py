from tkinter import *
from constants import constants

window = Tk()
window.title(constants.WINDOW_TITLE)
window.config(width=constants.CARD_WIDTH, height=constants.CARD_HEIGHT)
button_x = Button(window)
button_check = Button(window)

card = Canvas(window, width=constants.CARD_WIDTH, height=constants.CARD_HEIGHT, bg="white")
card.grid(row=0, column=0, columnspan=2)
button_x.grid(row=0, column=0)
button_check.grid(row=1, column=1)

# must be at the bottom of the file
window.mainloop()