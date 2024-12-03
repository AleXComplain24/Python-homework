from PIL import Image, ImageFilter

# 1. Открытие и изменение размера изображения
image = Image.open('example.jpg')
image_resized = image.resize((300, 300))
image_resized.show()

# 2. Применение фильтра размытия
image_blurred = image.filter(ImageFilter.BLUR)
image_blurred.show()

# 3. Сохранение изображения в другом формате
image_resized.save('example_resized.png')
print("Изображение сохранено в формате PNG.")
