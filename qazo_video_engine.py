import random
from datetime import datetime
from pathlib import Path

# --- إعدادات إمبراطورية Qazo ---
AFFILIATE_LINK = "https://amzn.to/qazo_gaming"

GAME_TOPICS = [
    {
        "title": "أسرار خفية مرعبة في ألعاب العالم المفتوح لم تنتبه لها!",
        "thumbnail": "https://img.youtube.com/vi/sample_thumb_1/maxresdefault.jpg",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    },
    {
        "title": "توب 10 أخطاء مطورية في الألعاب تحولت لمزايا أسطورية عشقها اللاعبون!",
        "thumbnail": "https://img.youtube.com/vi/sample_thumb_2/maxresdefault.jpg",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4"
    },
    {
        "title": "ليش هذا السر في لقطات الـ Rocket League غيّر موازين الاحتراف؟",
        "thumbnail": "https://img.youtube.com/vi/sample_thumb_3/maxresdefault.jpg",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
    }
]

def build_qazo_empire():
    print("🚀 جاري بدء تشغيل مصنع Qazo الشامل...")
    
    # اختيار مقطعين عشوائيين
    selected = random.sample(GAME_TOPICS, 2)
    now_str = datetime.now().strftime('%Y-%m-%d | %I:%M %p')
    
    # بناء محتوى الداشبورد بالكامل بداخل متغير نصي ضخم
    lines = []
    lines.append("# لوحة تحكم إمبراطورية Qazo")
    lines.append(f"> آخر تحديث: {now_str}")
    lines.append("> الحالة: جاهز للنشر اليدوي الآمن 🚀\n")
    lines.append("---")
    
    for idx, item in enumerate(selected, 1):
        final_title = item['title'] + " #Qazo"
        desc = (
            "استكشف معنا أسرار وخبايا الألعاب الاحترافية!\n\n"
            "أدوات وتجهيزات الجيمنز (رابط العمولة):\n"
            f"- أفضل رخص ومعدات الألعاب: {AFFILIATE_LINK}"
        )
        
        lines.append(f"\n### المقطع رقم {idx}")
        lines.append(f"* العنوان المقترح:\n  > `{final_title}`")
        lines.append(f"* الوصف ورابط الأفلييت:\n  ```text\n  {desc}\n  ```")
        lines.append(f"* رابط الثمنيل (الصورة المصغرة): [عرض الصورة]({item['thumbnail']})")
        lines.append(f"* رابط تحميل الفيديو المباشر: [تحميل ملف الفيديو (MP4)]({item['video_url']})\n")
        lines.append("---")
    
    full_text = "\n".join(lines)
    
    # الكتابة المباشرة في ملف dashboard.md
    target_file = Path("dashboard.md")
    target_file.write_text(full_text, encoding="utf-8")
    
    print("✅ تم توليد وتعبئة ملف dashboard.md بالكامل بنجاح!")

if __name__ == "__main__":
    build_qazo_empire()
