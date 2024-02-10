from PIL import Image
import os

# Папка с изображениями
folder = "maps"

# Получаем список всех файлов в папке
files = os.listdir(folder)

# Открываем первое изображение для получения размеров
first_image = Image.open(os.path.join(folder, files[0]))
width, height = first_image.size

# Создаем новое изображение-контейнер для объединения
result_image = Image.new('RGB', (width * 10, height * 10))

# Итерируемся по всем файлам и вставляем их в общее изображение
for index, file in enumerate(files):
    # Открываем текущее изображение
    current_image = Image.open(os.path.join(folder, file))
    
    # Определяем позицию в общем изображении
    x = (index // 11) * width
    y = (index % 11) * height
    
    # Вставляем текущее изображение в общее изображение
    result_image.paste(current_image, (x, y))

# Сохраняем объединенное изображение
result_image.save(os.path.join(folder, "combined_image.jpg"))

print("Объединенное изображение сохранено.")