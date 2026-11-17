import os
import random
from datetime import datetime

# إعدادات روابط التسويق بالعمولة (Amazon Affiliate) ومواضيع Qazo
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

def generate_dashboard():
    selected_topics = random.sample(GAME_TOPICS, 2)
    current_time = datetime.now().strftime('%Y-%m-%d | %I:%M %p')
    
    dashboard_content = "# لوحة تحكم إمبراطورية Qazo\n"
    dashboard_content += "> آخر تحديث: " + current_time + "\n"
    dashboard_content += "> الحالة: جاهز للنشر اليدوي الآمن 🚀\n\n---\n"

    for i, topic in enumerate(selected_topics, 1):
        title = topic['title'] + " #Qazo"
        description = "استكشف معنا أسرار وخبايا الألعاب الاحترافية!\n\nأدوات وتجهيزات الجيمنز (رابط العمولة):\n- أفضل رخص ومعدات الألعاب: " + AFFILIATE_LINK
        
        dashboard_content += "\n### المقطع رقم " + str(i) + "\n"
        dashboard_content += "* العنوان المقترح:\n  > `" + title + "`\n"
        dashboard_content += "* الوصف ورابط الأفلييت:\n  ```text\n  " + description + "\n  ```\n"
        dashboard_content += "* رابط الثمنيل (الصورة المصغرة): [عرض الصورة](" + topic['thumbnail'] + ")\n"
        dashboard_content += "* رابط تحميل الفيديو المباشر: [تحميل ملف الفيديو (MP4)](" + topic['video_url'] + ")\n\n---\n"

    with open("dashboard.md", "w", encoding="utf-8") as f:
        f.write(dashboard_content)
    
    print("✨ تم تحديث لوحة تحكم Qazo بنجاح وجهزت مقطعين اليوم!")

if __name__ == "__main__":
    generate_dashboard()
