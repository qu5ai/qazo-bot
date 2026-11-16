from PIL import Image, ImageDraw, ImageFont
import os

def generate_qazo_thumbnail(title_text, category_label="التحليلي", output_path="qazo_thumb.png"):
    # مقاسات يوتيوب القياسية للصورة المصغرة (1280x720)
    width, height = 1280, 720
    
    # خلفية داكنة وفخمة تتماشى مع جو القناة والجيمنج
    image = Image.new("RGB", (width, height), color=(20, 20, 30))
    draw = ImageDraw.Draw(image)
    
    # استخدام خط Tajawal-Bold الذي رفعته لمستودعك
    font_path = "Tajawal-Bold.ttf"
    try:
        title_font = ImageFont.truetype(font_path, 70)
        label_font = ImageFont.truetype(font_path, 50)
    except IOError:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        
    # رسم شريط علوي أبيض تماماً مثل تصميمك الأصلي
    draw.rectangle([0, 0, width, 100], fill=(255, 255, 255))
    
    # كتابة التصنيف العلوي (مثل: التحليلي، القيادي، المسالم) في المنتصف العلوي
    draw.text((width // 2 - 120, 20), category_label, fill=(0, 0, 0), font=label_font)
    
    # كتابة العنوان الرئيسي في منتصف الصورة بخلفية واضحة
    draw.rectangle([100, 420, width - 100, 600], fill=(0, 0, 0, 200))
    draw.text((120, 450), title_text, fill=(255, 255, 255), font=title_font)
    
    # حفظ الصورة المصغرة النهائية
    image.save(output_path)
    print(f"تم إنشاء الصورة المصغرة باستخدام خط Tajawal-Bold وحفظها في: {output_path}")

if __name__ == "__main__":
    generate_qazo_thumbnail("كيف تحترف برمجة الألعاب؟", "التحليلي")
