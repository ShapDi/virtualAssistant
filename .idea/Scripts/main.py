from Front.main_window import MainWindow
from Back.recognizer import listen

import Back.recognizer

def main():
    window = MainWindow()
    window.set_recognizer(recognizer=Back.recognizer)
    window.create()

if __name__ == '__main__':
    main()