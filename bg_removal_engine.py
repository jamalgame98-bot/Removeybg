from rembg import remove
from PIL import Image
import os

# --- الإعدادات ---
input_file = 'test.png'  # تأكدت باللي السمية والصيغة صحيحة (png)
output_file = 'result_no_bg.png'

def start_engine():
    # 1. التشييك واش الصورة كاينة بصح
    if not os.path.exists(input_file):
        print(f"❌ خطأ: مالقيتش الملف '{input_file}' وسط الدوسي EasyREMB.")
        return

    try:
        print("🚀 جاري معالجة الصورة... (إيلا كانت أول مرة، غادي يتسنى يتيليشارجي الموديل)")
        
        # 2. فتح الصورة
        with open(input_file, 'rb') as i:
            input_data = i.read()
            
            # 3. إزالة الخلفية بالذكاء الاصطناعي
            output_data = remove(input_data)
            
            # 4. حفظ النتيجة
            with open(output_file, 'wb') as o:
                o.write(output_data)
        
        print(f"✅ ناضي! الصورة تنقات وتحفظات سميتها: {output_file}")
        print("🔗 تقدر دابا تفتح الدوسي وتشوف النتيجة.")

    except Exception as e:
        print(f"❌ وقع مشكل تقني: {e}")

# تشغيل المحرك
if __name__ == "__main__":
    start_engine()