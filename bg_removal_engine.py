import telebot
from rembg import remove
from PIL import Image
import io
import os

# الساروت ديالك اللي عطيتي ليا
TOKEN = '8238787092:AAHPlHZeE3woH2t-q14LUYhg8AynYD2aX1E'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً يا جمال! صيفط ليا دابا أي صورة وغادي نحيد ليها الخلفية في ثانية. 🚀")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # إشعار للمستخدم ببدء الخدمة
        msg = bot.reply_to(message, "جاري تنقية الصورة... انتظر لحظة ⏳")
        
        # تحميل الصورة
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # معالجة الصورة بالذكاء الاصطناعي
        input_image = Image.open(io.BytesIO(downloaded_file))
        output_image = remove(input_image)
        
        # تحويل النتيجة لملف جاهز للإرسال
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # إرسال النتيجة كملف (Document) باش تبقى الجودة عالية
        bot.send_document(message.chat.id, img_byte_arr, visible_file_name='no-bg-jamal.png')
        bot.delete_message(message.chat.id, msg.message_id)
        
    except Exception as e:
        bot.reply_to(message, "وقع مشكل تقني، جرب صورة أخرى.")
        print(f"Error: {e}")

# هاد الجزء ضروري لـ Render باش ما يسدش السيرفر
if __name__ == "__main__":
    print("البوت خدام دابا... صيفط ليه تصويرة!")
    bot.infinity_polling()
