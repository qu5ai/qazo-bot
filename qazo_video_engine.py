import os
import random
from datetime import datetime

# إعدادات روابط التسويق بالعمولة (Amazon Affiliate) ومواضيع Qazo
AFFILIATE_LINK = "https://amzn.to/qazo_gaming"

GAME_TOPICS = [
    {
        "title": "أسرار خفية مرعبة في ألعاب العالم المفتوح لم تنتبه لها! 🤯🎮",
        "thumbnail": "https://img.youtube.com/vi/sample_thumb_1/maxresdefault.jpg",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    },
    {
        "title": "توب 10 أخطاء مطورية في الألعاب تحولت لمزايا أسطورية عشقها اللاعبون! ⚡",
        "thumbnail": "https://img.youtube.com/vi/sample_thumb_2/maxresdefault.jpg",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4"
    },
    {
        "title": "ليش هذا السر في لقطات الـ Rocket League غيّر موازين الاحتراف؟ 🚀",
        "thumbnail": "https://img.youtube.com/vi/sample_thumb_3/maxresdefault.jpg",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
    }
]

def generate_dashboard():
    # اختيار مقطعين عشوائيين لكل يوم (مرتين في اليوم)
    selected_topics = random.sample(GAME_TOPICS, 2)
    current_time = datetime.now().strftime('%Y-%m-%d | %I:%M %p')
    
    # تصميم واجهة التطبيق/لوحة التحكم المرتبة
    dashboard_content = "# 🎬 لوحة تحكم إمبراطورية Qazo\n"
    dashboard_content += f"> **آخر تحديث:** {current_time}  \n"
    dashboard_content += "> **الحالة:** جاهز للنشر اليدوي الآمن 🚀\n\n---\n"

    for i, topic in enumerate(selected_topics, 1):
        title = f"{topic['title']} #Qazo"
        description = f"استكشف معنا أسرار وخ
