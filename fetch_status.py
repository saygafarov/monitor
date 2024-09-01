import requests
import json
import time


def fetch_statuses(text_widget, stop_thread_flag):
    """
    Функция для выполнения запросов к API и обновления текстового виджета статусами сервисов.

    :param text_widget: Tkinter текстовый виджет для вывода статусов
    :param stop_thread_flag: Флаг остановки потока
    """

    url = 'http://localhost:9521/api/services/status'
    headers = {
        'Authorization': 'Basic YWRtaW46JHNpZ3VyI2FkbWluJA=='
    }

    while not stop_thread_flag['stop']:
        try:
            # Выполнение GET-запроса
            response = requests.get(url, headers=headers)

            # Проверка статуса ответа
            if response.status_code == 200:
                services_status = json.loads(response.text)

                # Очистка текстового виджета перед выводом новых данных
                text_widget.delete(1.0, 'end')

                # Обновление статусов
                for service in services_status:
                    service_id = service['id']
                    health_status = service['status']['health']

                    # Вывод статуса в текстовый виджет
                    text_widget.insert('end', f"{service_id} статус: {health_status}\n")
            else:
                text_widget.insert('end', f"Ошибка: получен статус-код {response.status_code}\n")

            # Пауза на 3 секунд между запросами
            time.sleep(3)

        except Exception as e:
            text_widget.insert('end', f"Ошибка: {e}\n")
            time.sleep(3)
