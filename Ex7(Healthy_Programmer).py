from pygame import mixer
from time import time
from datetime import datetime


def call(sound, stop, word):
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()
    while True:
        a = input(f"Enter '{stop}' if you have {word}.\n")
        a = a.lower()
        if a == stop:
            mixer.music.stop()
            break


def log(date_time):
    with open("Ex7(Log_file).txt", "a") as f:
        f.write(f"{date_time} {datetime.now()}\n")
        print("Successfully recorded.")


if __name__ == "__main__":
    water_time1 = time()
    exercise_time1 = time()
    eyerest_time1 = time()
    water_time2 = 40*60
    exercise_time2 = 30*60
    eyerest_time2 = 45*60
    pass


while True:
    if time() - water_time1 > water_time2:
        call("water.mp3", "drank", "drank the water")
        water_time1 = time()
        log("Drank water at")

    elif time() - exercise_time1 > exercise_time2:
        call("bomb-falling-and-exploding-01.mp3", "done", "done  the exercise")
        exercise_time1 = time()
        log("Done exercise at")

    elif time() - eyerest_time1 > eyerest_time2:
        call("bell-ringing-03.mp3", "done", "rested your eyes")
        eyerest_time1 = time()
        log("Rested eyes at")     
