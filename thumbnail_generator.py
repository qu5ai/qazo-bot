from PIL import Image, ImageDraw, ImageFont
import os

def generate_qazo_thumbnail(title_text, output_path="qazo_thumb.png"):
    # مقاسات يوتيوب القياسية للصور المصغرة (1280x720)
    width, height = 1280, 720
    
    # إنشاء خلفية داكنة وجذابة تناسب الجيمنج (تدرج لوني أو لون داكن فخم)
    image = Image.new("RGB", (width, height), color=(15, 15, 25))
    draw = ImageDraw.Draw(image)
    
    # رسم إطار أو لمسة جمالية في الخلفية لزيادة الحيوية
    draw.rectangle([30, 30, width - 30, height - 30], outline=(0, 204, 255), width=6)
    
    # إضافة نص العنوان (ملاحظة: ليدعم الخط العربي بشكل مثالي على السيرفر، يفضل استخدام ملف خط TTF مثل Amiri أو Cairo)
    font_path = "Cairo-Bold.ttf"  # تأكد من توفر ملف الخط في المشروع، أو استخدم الخط الافتراضي
    try:
        font = ImageFont.truetype(font_path, 65)
    except IOError:
        font = ImageFont.load_default()
        
    # تقسيم النص وتنسيقه ليظهر بمنتصف الصورة
    # (يمكننا إضافة معالجة النصوص العربية وعكسها إذا لزم الأمر لتظهر الحروف متصلة بشكل صحيح)
    text_color = (255, 255, 255)
    
    # رسم شريط خلف النص لزيادة الوضوح
    draw.rectangle([80, 420, width - 80, 600], fill=(0, 0, 0, 180))
    
    # كتابة العنوان على الصورة
    draw.text((100, 450), title_text, fill=text_color, font=font)
    
    # حفظ الصورة الناتجة
    image.save(output_path)
    print(f"تم بنجاح توليد الصورة المصغرة وحفظها في: {output_path}")

if __name__ == "__main__":
    # تجربة توليد صورة بعنوان افتراضي
    generate_qazo_thumbnail("كيف تحترف برمجة الألعاب في 2026؟")
