import telebot
from rembg import remove
from PIL import Image
import io
import os

# الساروت ديالك (الـ Token)
TOKEN = '8238787092:AAHPlHZeE3woH2t-q14LUYhg8AynYD2aX1E'

bot = telebot.TeleBot(TOKEN)

# كود ترحيبي
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً يا جمال! صيفط ليا دابا أي صورة وغادي نحيد ليها الخلفية في ثانية. 🚀")

# معالجة الصور المرسلة
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # إشعار للمستخدم
        msg = bot.reply_to(message, "جاري تنقية الصورة... انتظر لحظة ⏳")
        
        # تحميل الصورة من تيليجرام
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # تحويل لـ PIL Image
        input_image = Image.open(io.BytesIO(downloaded_file))
        
        # إزالة الخلفية بالذكاء الاصطناعي
        output_image = remove(input_image)
        
        # تحويل النتيجة لملف PNG جاهز للإرسال
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # إرسال النتيجة كملف (بجودة عالية)
        bot.send_document(message.chat.id, img_byte_arr, visible_file_name='Removeybg_Result.png')
        
        # مسح رسالة الانتظار
        bot.delete_message(message.chat.id, msg.message_id)
        
    except Exception as e:
        bot.reply_to(message, "وقع مشكل تقني، جرب صورة أخرى.")
        print(f"Error logic: {e}")

# تشغيل البوت (Polling) - هادشي اللي كايخلي السيرفر خدام
if __name__ == "__main__":
    print("الماكينة ناضية... البوت متصل دابا!")
    # infinity_polling كايخليه ما يوقفش وخا يوقع خطأ بسيط
    bot.infinity_polling()
