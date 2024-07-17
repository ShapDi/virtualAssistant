from Scripts.Front.main_window import MainWindow
from Scripts.Back.recognizer import listen
import Scripts.Back.recognizer

def main():
    window = MainWindow(recognizer=Scripts.Back.recognizer)
    window.create()

if __name__ == '__main__':
    main()
