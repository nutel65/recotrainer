import time
import sys
import random
import msvcrt

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def exit():
    sys.exit()

def basic_help():
    print(
"""
--- Recotrainer ---
Narzędzie do ćwiczenia gry na flecie.
Dostępne są następujące komendy:
   'nuty' - ćwicz pojedyńcze nuty
   'skale' - ćwicz całe skale
   'pomoc' - dodatkowe informacje w razie kłopotów
   'wyjdz' - wyjście z programu"""
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
    print("wpisz prędkość wyświetlania nut w milisekundach, "
          "polecam '3000' na start")
    change_rate = None
    while not change_rate:
        try:
            inp = int(input("> "))
            if 5000 > inp > 500:
                change_rate = inp
            else:
                print("Wprowadź wartość z przedziału (500 - 5000)")
        except ValueError:
            print("Wprowadzono niepoprawną wartość. "
                  "Wybierz nową wartość (np. 2000)")
    return change_rate


def scale_trainer():
    # change_rate = input_change_rate()
    print("opcja niedostępna")

def note_trainer():
    change_rate = input_change_rate()
    running = True
    note_count = 0
    start_time = time.time()
    print("Aby wyjść naciśnij ESC")
    print("================")
    print("NUTA DO ZAGRANIA:\n")
    while running:
        print(f"\r\t{random.choice(NOTES)}", end=' ')
        if msvcrt.kbhit() and msvcrt.getch().decode() == chr(27):
            running = False
        note_count += 1
        time.sleep(change_rate/1000)
    print(f"\nĆwiczono {int(time.time() - start_time)} sekund "
          f"i zagrano {note_count} nut.")
    time.sleep(1)
    basic_help()

def main():
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
        else:
            basic_help()

if __name__ == "__main__":
    main()
