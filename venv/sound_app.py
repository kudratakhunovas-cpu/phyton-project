import tkinter as tk
from tkinter import PhotoImage
import pygame
import os

# ИНИЦИАЛИЗАЦИЯ PYGAME
pygame.mixer.init()

# БАЗОВАЯ ПАПКА ПРОЕКТА
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(file):
    return os.path.join(BASE_DIR, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# СОЗДАНИЕ КНОПОК (КАРТИНКА + ЗВУК)
def create_btn(root, img_path, sound_path):
    img = PhotoImage(file=img_path)
    btn = tk.Button(root, image=img, command=lambda: play_sound(sound_path),
                    border=0, highlightthickness=0)
    return btn, img

# ГЛАВНОЕ ОКНО
def create_app():
    root = tk.Tk()
    root.title("Cartoon Sounds")
    root.geometry("350x500")
    root.resizable(False, False)

    images = []   # чтобы картинки не удалялись

    buttons_data = [
        ("assets/img/mickey.png", "assets/sounds/mickey.mp3"),
        ("assets/img/minion.png", "assets/sounds/minion.mp3"),
        ("assets/img/shrek.png", "assets/sounds/shrek.mp3"),
        ("assets/img/nemo.png", "assets/sounds/nemo.mp3"),
        ("assets/img/panda.png", "assets/sounds/panda.mp3"),
    ]

    for img_path, snd_path in buttons_data:
        btn, pic = create_btn(root, abs_path(img_path), abs_path(snd_path))
        btn.pack(pady=10)
        images.append(pic)

    root.mainloop()

create_app()
