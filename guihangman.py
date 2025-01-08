#hackr.io
import tkinter as tk
import random

class Hangman:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("900*600")
        self.word_list = ["MOTHER", "FATHER", "SISTER", "BROTHER", "GRANDMOTHER", "GRANDFATHER", "UNCLE", "AUNT", "COUSIN", "NEPHEW", "NIECE", "DAUGHTER", "SON", "GRANDDAUGHTER", "GRANDSON", "FRIEND", "ENEMY", "TEACHER", "STUDENT", "DOCTOR", "NURSE", "ENGINEER", "SCIENTIST", "ARTIST", "MUSICIAN", "ACTOR", "ACTRESS", "DANCER", "SINGER", "WRITER", "POET", "ATHLETE", "COACH",]
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.initialize_gui()
        #GUI setup and GameLogic after this

    def choose_secret_word(self):
        return random.choice(self.word_list)

    def initialize_gui(self):
        self.hangman_canvas = tk.canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pasdy=20)
        #Add GUI setup continue

    def initialize_gui(self):
        self.word_display = tk.Label(self.master, text="_"*len(self.secret_word),font=("Helvetica",30))
        self.word_display.pack(pady=(40,20))

    def initialize_gui(self):
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        self.setup_alphabet_buttons()


def main():
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()

if __name__=="__main__":
    main()
