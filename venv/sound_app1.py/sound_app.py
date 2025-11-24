import tkinter as tk
from tkinter import PhotoImage
import pygame
import os

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(folder, file):
    return os.path.join(BASE_DIR, folder, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def create_app():
    root = tk.Tk()
    root.title("Sound & Images")
    root.geometry("350x400")
    root.resizable(False, False)

    img1 = PhotoImage(file=abs_path("images", "pic1.png"))
    img2 = PhotoImage(file=abs_path("images", "pic2.png"))

    tk.Button(root, image=img1,
              command=lambda: play_sound(abs_path("sounds", "sound1.mp3"))
              ).pack(pady=10)

    tk.Button(root, image=img2,
              command=lambda: play_sound(abs_path("sounds", "sound2.mp3"))
              ).pack(pady=10)

    tk.Button(root, text="Звук 3", font=("Arial", 14),
              command=lambda: play_sound(abs_path("sounds", "sound3.mp3"))
              ).pack(pady=10)

    tk.Button(root, text="Звук 4", font=("Arial", 14),
              command=lambda: play_sound(abs_path("sounds", "sound1.mp3"))
              ).pack(pady=10)

    tk.Button(root, text="Звук 5", font=("Arial", 14),
              command=lambda: play_sound(abs_path("sounds", "sound2.mp3"))
              ).pack(pady=10)

    root.mainloop()

create_app()
