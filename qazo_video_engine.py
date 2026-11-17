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

def generate_qazo_txt():
    selected = random.sample(GAME_TOPICS, 2)
    now_str = datetime.now().strftime('%Y-%m-%d | %I:%M %p')
    
    content = f"=== محتوى إمبراطورية Qazo اليومي ===\n"
    content += f"التاريخ والوقت: {now_str}\n"
    content += f"=====================================\n\n"
    
    for idx, item in enumerate(selected, 1):
        final_title = item['title'] + " #Qazo"
        desc = (
            "استكشف معنا أسرار وخبايا الألعاب الاحترافية!\n\n"
            "أدوات وتجهيزات الجيمنز (رابط العمولة):\n"
            f"- أفضل رخص ومعدات الألعاب: {AFFILIATE_LINK}"
        )
        
        content += f"[ المقطع رقم {idx} ]\n"
        content += f"العنوان:\n{final_title}\n\n"
        content += f"الوصف ورابط الأفلييت:\n{desc}\n\n"
        content += f"رابط الثمنيل:\n{item['thumbnail']}\n\n"
        content += f"رابط الفيديو (MP4):\n{item['video_url']}\n"
        content += f"-------------------------------------\n\n"

    # كتابة الملف النصي الصافي مباشرة
    file_path = Path("qazo.txt")
    file_path.write_text(content, encoding="utf-8")
    print("تم إنشاء ملف qazo.txt بنجاح!")

if __name__ == "__main__":
    generate_qazo_txt()
