import tkinter as tk
from tkinter import scrolledtext
import threading
from fetch_status import fetch_statuses


def start_fetching(text_widget, stop_thread_flag):
    """
    Функция для запуска потока с запросами к API.

    :param text_widget: Tkinter текстовый виджет для вывода статусов
    :param stop_thread_flag: Флаг остановки потока
    """

    stop_thread_flag['stop'] = False
    thread = threading.Thread(target=fetch_statuses, args=(text_widget, stop_thread_flag))
    thread.start()
    return thread


def stop_fetching(stop_thread_flag, thread):
    """
    Функция для остановки потока с запросами к API.

    :param stop_thread_flag: Флаг остановки потока
    :param thread: Поток, который нужно остановить
    """

    stop_thread_flag['stop'] = True
    thread.join()  # Ждем завершения потока


def create_gui():
    """
    Функция для создания графического интерфейса.
    """

    root = tk.Tk()
    root.title("Monitor")

    # Текстовый виджет для вывода статусов
    text_widget = scrolledtext.ScrolledText(root, width=50, height=20)
    text_widget.pack(pady=10)

    # Инициализация переменных для управления потоком
    stop_thread_flag = {'stop': False}
    thread = None

    # Кнопки управления
    start_button = tk.Button(root, text="Старт", command=lambda: start_fetching(text_widget, stop_thread_flag))
    start_button.pack(side=tk.LEFT, padx=20)

    stop_button = tk.Button(root, text="Стоп", command=lambda: stop_fetching(stop_thread_flag, thread))
    stop_button.pack(side=tk.RIGHT, padx=20)

    # Функция для управления началом и окончанием работы потоков
    def manage_thread():
        nonlocal thread
        if not stop_thread_flag['stop'] and (thread is None or not thread.is_alive()):
            thread = start_fetching(text_widget, stop_thread_flag)

    root.after(100, manage_thread)
    root.mainloop()
