import requests
from telegram import Bot
from image_creator import create_usd_image
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("6801560559:AAG__a1frsk7FhhAvrDVCXM7bS4e6mtoIZw")
CHANNEL_ID = os.getenv("https://t.me/Tundizayn")

def get_usd_rate():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item["Ccy"] == "USD":
            return item["Rate"]
    return "Noma'lum"

def main():
    rate = get_usd_rate()
    img_path = create_usd_image(rate)

    bot = Bot(token=BOT_TOKEN)

    caption = f"📅 Sana: {get_today()}\n💵 1 USD = {rate} so‘m\n📊 Manba: https://cbu.uz\n#dollarkursi"

    with open(img_path, "rb") as photo:
        bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=caption)

def get_today():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    main()
