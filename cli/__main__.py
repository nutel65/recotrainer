import time
import sys
import os
import random
import msvcrt
import json

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
NOTES2 = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
SETTINGS = None

def create_settings_file():
    default_settings = {
        "b_notation": False,
        "show_help": True,
        "show_stats": True,
    }
    with open("settings.json", 'w') as json_file:
        json.dump(default_settings, json_file, indent=4, sort_keys=True)

def load_settings():
    global SETTINGS
    try:
        with open("settings.json", 'r') as json_file:
            SETTINGS = json.load(json_file)
    except (IOError, json.decoder.JSONDecodeError) as e:
        print(f"settings.json loading error: {e}")
        print("Reverting default configuration...")
        create_settings_file()
        print("Restarting the program to apply changes...")
        main()

def exit():
    sys.exit()

def basic_help():
    print(
"""
=======================RecoTrainer=======================
Narzędzie do ćwiczenia gry na flecie.
Dostępne są następujące komendy:
   'nuty' - ćwicz pojedyńcze nuty
   'skale' - ćwicz całe skale
   'pomoc' - dodatkowe informacje w razie kłopotów
   'ustawienia' - zmień sposób działania programu
   'wyjdz' - wyjście z programu"""
    )

def settings_screen():
    print(
"""
========================USTAWIENIA=======================
Aby zmienić ustawienie wypisz [numer]:[true/false] np. 3:true
    [1] stosowanie notacji z 'b' zamiast '#': {0}
    [2] pokazuj pomoc na każdym ekranie: {1}
    [3] wyświetlaj czas po każdym ćwiczeniu: {2}
""".format(SETTINGS["b_notation"], SETTINGS["show_help"], SETTINGS["show_stats"])
    )

def verbose_help():
    basic_help()
    print(
"""
Trener nut:
...
Trener skal:
..."""
    )

def input_change_rate():
    print("Określ prędkość wyświetlania nut w milisekundach, "
          "polecam '3000' na start:")
    change_rate = None
    while not change_rate:
        try:
            inp = int(input("> "))
            if 5000 >= inp >= 500:
                change_rate = inp
            else:
                print("Wprowadź wartość z przedziału (500 - 5000)")
        except ValueError:
            print("Wprowadzono niepoprawną wartość. "
                  "Wpisz nową wartość (np. 2000)")
    return change_rate

def scale_trainer():
    # change_rate = input_change_rate()
    print("opcja niedostępna")

def note_trainer():
    change_rate = input_change_rate()
    running = True
    note_count = 0
    start_time = time.time()
    print("Aby wyjść naciśnij dowolny klawisz")
    print("================")
    print("NUTA DO ZAGRANIA:\n")
    while running:
        if msvcrt.kbhit() and msvcrt.getch():
            running = False
        print(f"\r\t{random.choice(NOTES)}\t", end='')
        note_count += 1
        time.sleep(change_rate/1000)
        print("\r\t  \t", end='')

    print(f"\nĆwiczono {int(time.time() - start_time)} sekund "
          f"i zagrano {note_count} nut.")
    time.sleep(1)
    basic_help()

def main():
    load_settings()
    basic_help()
    # main loop
    while True:
        user_input = input("> ").lower()
        if user_input == "nuty":
            note_trainer()
        elif user_input == "skale":
            scale_trainer()
        elif user_input in ("pomoc", "help"):
            verbose_help()
        elif user_input in ("wyjdz", "exit", "quit"):
            exit()
        elif user_input == "ustawienia":
            settings_screen()
        else:
            basic_help()

if __name__ == "__main__":
    main()
