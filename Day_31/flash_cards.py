import random
import time

import pandas
from tkinter import *
from gtts import gTTS
import os
import vlc
import playsound
from pygame import mixer

# constants
BACKGROUND = '#B0DBC4'
TEXT_WHITE = '#FFFFFF'
LANGUAGE_X = 400
LANGUAGE_Y = 150
TITLE_X = 400
TITLE_Y = 150
TEXT_X = 400
TEXT_Y = 263
TITLE_FONT = ('Ariel', 40, 'italic')
TEXT_FONT = ('Ariel', 60, 'bold')
TITLE_TAG = 'title'
TEXT_TAG = 'text'

current_card = {}
is_english = True
flip_timer = ""
# files

csv_data = pandas.read_csv('./data/french_words.csv')
french_english_words_list = csv_data.to_dict(orient='records')

csv_data = pandas.read_csv('./data/tamil_words.csv')
tamil_english_words_list = csv_data.to_dict(orient='records')

with open('hehe.mp3', 'w') as file:
    tts = gTTS(text='You suck', lang='en')
    file1 = str('hehe.mp3')
    tts.save(file1)


def generate_random_index():
    return random.randint(0, len(french_english_words_list))


def tts():
    global is_english
    if is_english:
        word = current_card['English']
        lang = 'en'
    else:
        word = current_card['Tamil']
        lang = 'ta'

    r = random.randint(0, 100)
    tts = gTTS(text=word, lang=lang)
    file1 = str("lol" + str(r) + ".mp3")
    tts.save(file1)
    mixer.init()
    mixer.music.load(file1)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.music.load('hehe.mp3')
    os.remove(file1)

def flip_card():
    global is_english, current_card
    if is_english:
        is_english = False
        canvas.itemconfig(card_bg, image=card_front)
        canvas.itemconfig(card_title, text='Tamil', fill='black')
        canvas.itemconfig(card_word, text=current_card['Tamil'], fill='black')
    else:
        is_english = True
        canvas.itemconfig(card_bg, image=card_back)
        canvas.itemconfig(card_title, text='English', fill=TEXT_WHITE)
        canvas.itemconfig(card_word, text=current_card['English'], fill=TEXT_WHITE)


def show_card():
    global current_card, flip_timer, is_english
    current_card = random.choice(tamil_english_words_list)
    is_english = False
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text='Tamil', fill='black')
    canvas.itemconfig(card_word, text=current_card['Tamil'], fill='black')
    #flip_timer = window.after(3000, func=flip_card)


window = Tk()
window.title('Flash card generator')
window.config(padx=50, pady=50, bg=BACKGROUND)
# canvas

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')

canvas = Canvas(width=800, height=600, highlightthickness=0, bg=BACKGROUND)

card_bg = canvas.create_image(400, 300, image=card_front)

card_title = canvas.create_text(TITLE_X, TITLE_Y, text="Tamil", font=TITLE_FONT, tags=TITLE_TAG)
card_word = canvas.create_text(TEXT_X, TEXT_Y, text='Word', font=TEXT_FONT, tags=TEXT_TAG)
canvas.grid(row=0, column=0, rowspan=2, columnspan=2)

# buttons
speech_icon = PhotoImage(file='./images/sound (1).png')
speech_btn = Button(
    image=speech_icon,
    highlightthickness=0,
    bg=BACKGROUND,
    relief=GROOVE,
    command=tts
)
speech_btn.grid(row=0, column=2, sticky='e')

flip_icon = PhotoImage(file='./images/flip (1).png')
flip_btn = Button(
    text='FLIP',
    font=('Ariel', 16, 'bold'),
    highlightthickness=0,
    bg=BACKGROUND,
    relief=GROOVE,
    width=4,
    height=2,
    command=flip_card
)
flip_btn.grid(row=1, column=2, sticky='e')

correct_btn_img = PhotoImage(file='./images/right.png')
correct_btn = Button(image=correct_btn_img, highlightthickness=0, bg=BACKGROUND, relief=GROOVE, command=show_card)
correct_btn.grid(row=2, column=0, columnspan=2)

show_card()

window.mainloop()
