import json
import time

import requests

url = 'http://localhost:9521/api/services/status'
headers = {
    'Authorization': 'Basic YWRtaW46JHNpZ3VyI2FkbWluJA=='
}

try:
    while True:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            services_status = json.loads(response.text)

            for service in services_status:
                service_id = service['id']
                health_status = service['status']['health']

                print(f'{service_id} статутс: {health_status}')

        else:
            print(f"Ошибка: получен статус-код {response.status_code}")

        time.sleep(3)

except KeyboardInterrupt:
    print('Application closed')
