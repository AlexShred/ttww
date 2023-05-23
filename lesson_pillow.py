from PIL import Image, ImageDraw, ImageFont

file_pass = 'media/jelly.png'


image = Image.open(file_pass)

# показать изображение
#
# image.show()
#

# обрезка изображения
#
# cropped_image = image.crop((0, 80, 200, 400))
#
# cropped_image.save('media/jelly_cropped.png')
#

# # поворот изображения
# rottated_image = image.rotate(90)
# rottated_image.save('media/jelly_rottated.png')

# воднка
# img_draw = ImageDraw.Draw(image)
# text = 'This is Codify property'
# font = ImageFont.truetype('arial.ttf', size=32)
#
# img_draw.text((10, 10), text, font=font)
#
# image.save('media/jelly_watermark.png')


# image.save('media/jelly.webp', 'webp')



# конвертация изображения
# image = image.convert('RGB')
# image.save('media/jelly.jpg', 'JPEG')

#
# изменения разрешения
# image_resized = image.resize((400, 400))
# image_resized.save('media/jelly_resized.png')
#
# print(image.size)

width, height = image.size

# new_height = 300
# new_width = int(width * new_height / height)
#
# image_resized = image.resize(
#     (new_height, new_width)
# )
#
# image_resized.save('media/jelly_resized_correct.png')

new_width = 400
new_height = int(width * new_width / height)

image_resized = image.resize(
    (new_height, new_width)
)

image_resized.save('media/jelly_resized_correct11.png')

file_pass = 'media/jelly_resized_correct11.png'


image1 = Image.open(file_pass)

print(image1.size)