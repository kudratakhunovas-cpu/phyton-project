import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write

import tkinter as tk
from tkinter import filedialog
import threading

class Dictaphone:
    def __init__(self, sample_rate=44100, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio_data = None
        self.is_recording = False

    def record(self, duration=None):
        self.is_recording = True
        print("Начата запись...")

        if duration:
            self.audio_data = sd.rec(
                int(duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=self.channels
            )
            sd.wait()
            self.is_recording = False
            print("Запись завершена.")
        else:
            self.audio_data = []
            with sd.InputStream(
                samplerate=self.sample_rate,
                channels=self.channels,
                callback=self.callback
            ):
                while self.is_recording:
                    sd.sleep(100)

    def callback(self, indata, frames, time, status):
        self.audio_data.append(indata.copy())

    def stop(self):
        self.is_recording = False
        if isinstance(self.audio_data, list) and len(self.audio_data) > 0:
            self.audio_data = np.concatenate(self.audio_data, axis=0)
        print("Запись остановлена.")

    def save(self, filename="output.wav"):
        if self.audio_data is not None:
            write(filename, self.sample_rate,
                  (self.audio_data * 32767).astype(np.int16))
            print(f"Файл сохранён как: {filename}")
        else:
            print("Нет данных для сохранения.")

    def recognize_animal(self):
        """Распознавание: гав → собака, мяу → кот"""

        if self.audio_data is None:
            return "Нет записи"

        # временно сохраняем запись
        temp_file = "temp_audio.wav"
        write(temp_file, self.sample_rate,
              (self.audio_data * 32767).astype(np.int16))

        recognizer = sr.Recognizer()

        with sr.AudioFile(temp_file) as source:
            audio = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio, language="ru-RU").lower()
                print("Распознано:", text)

                if "гав" in text:
                    return "Это собака 🐶"
                elif "мяу" in text:
                    return "Это кот 🐱"
                else:
                    return "Животное не распознано 😕"

            except:
                return "Ошибка распознавания"


class DictaphoneApp:
    def __init__(self, master):
        self.master = master
        master.title("Диктофон + Определение животного")
        master.geometry("500x400")

        self.dictaphone = Dictaphone()

        self.label = tk.Label(master, text="Нажми Record для записи", font=("Arial", 14))
        self.label.pack(pady=10)

        self.record_btn = tk.Button(master, text="Record", command=self.start_recording)
        self.record_btn.pack(pady=5)

        self.stop_btn = tk.Button(master, text="Stop", command=self.stop_recording)
        self.stop_btn.pack(pady=5)

        self.save_btn = tk.Button(master, text="Save", command=self.save_recording)
        self.save_btn.pack(pady=5)

        self.detect_btn = tk.Button(master, text="Определить животное", command=self.detect_animal)
        self.detect_btn.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 16))
        self.result_label.pack(pady=10)

    def start_recording(self):
        thread = threading.Thread(target=self.dictaphone.record)
        thread.start()

    def stop_recording(self):
        self.dictaphone.stop()

    def save_recording(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav")]
        )
        if filename:
            self.dictaphone.save(filename)

    def detect_animal(self):
        result = self.dictaphone.recognize_animal()
        self.result_label.config(text=result)


if __name__ == "__main__":
    root = tk.Tk()
    app = DictaphoneApp(root)
    root.mainloop()
