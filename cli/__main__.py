import time
import sys
import random

def exit():
    sys.exit()

def basic_help():
    print(
        "--- Recotrainer ---\n"
        "Narzędzie do ćwiczenia gry na flecie."
        "Dostępne są następujące komendy:\n"
        "   `nuty` - ćwicz pojedyńcze nuty\n"
        "   `skale` - ćwicz skale\n"
        "   `pomoc` - dodatkowe informacje w razie kłopotów\n"
        "   `wyjdz` - wyjście z programu\n"
    )

def verbose_help():
    basic_help()
    print("Z czym jest problem?")

def scale_trainer():
    ...

def note_trainer():
    ...

def main():
    print(
        "--- Recotrainer ---\n"
        "Narzędzie do ćwiczenia gry na flecie."
        "Dostępne są następujące komendy:\n"
        "   `nuty` - ćwicz pojedyńcze nuty\n"
        "   `skale` - ćwicz skale\n"
        "   `pomoc` - dodatkowe informacje w razie kłopotów\n"
        "   `wyjdz` - wyjście z programu\n"
    )
    while True:
        user_input = input("> ")

if __name__ == "__main__":
    main()