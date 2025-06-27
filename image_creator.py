from PIL import Image, ImageDraw, ImageFont
import datetime
import os

def create_usd_image(rate):
    img = Image.new('RGB', (800, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    font_big = ImageFont.truetype("arial.ttf", 70)
    font_small = ImageFont.truetype("arial.ttf", 35)

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    draw.text((50, 80), "💵 1 USD =", font=font_big, fill=(0, 0, 0))
    draw.text((400, 80), f"{rate} so‘m", font=font_big, fill=(0, 100, 0))
    draw.text((50, 250), f"Sana: {today}", font=font_small, fill=(100, 100, 100))

    path = "usd_image.jpg"
    img.save(path)
    return path
