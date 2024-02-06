import requests
import os
import time

# Создаем папку maps, если её нет
if not os.path.exists('maps'):
    os.makedirs('maps')

# Диапазоны значений x и y
x_range = range(76540, 76551)
y_range = range(38220, 38231)

# URL-шаблон для загрузки изображений
url_template = "https://core-sat.maps.yandex.net/tiles?l=sat&v=2.1145.0&x={}&y={}&z=17&scale=2.0&lang=ru_RU&client_id=yandex-web-maps"

# Проходимся по всем значениям x и y
for x in x_range:
    for y in y_range:
        # Формируем URL для текущего значения x и y
        url = url_template.format(x, y)
        
        # Определяем имя файла
        filename = f"maps/{x}_{y}.jpeg"
        
        # Отправляем GET-запрос для загрузки изображения
        response = requests.get(url)
        
        # Проверяем успешность запроса
        if response.status_code == 200:
            # Сохраняем изображение в файл
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Сохранено изображение {filename}")
        else:
            print(f"Ошибка при загрузке изображения {url}: {response.status_code}")

        time.sleep(1)