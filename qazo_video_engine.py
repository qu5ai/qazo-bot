import os
import random
import requests
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
    }
]

def generate_qazo_content():
    # اختيار موضوع عشوائي بدون تكرار
    topic = random.choice(GAME_TOPICS)
    
    title = f"{topic['title']} | #{datetime.now().strftime('%d%H')}"
    description = f"استكشف معنا أسرار وخبايا الألعاب!\n\n🛒 أدوات وتجهيزات الجيمنز (رابط العمولة):\n- أفضل رخص ومعدات الألعاب: {AFFILIATE_LINK}"
    thumbnail = topic['thumbnail']
    video_url = topic['video_url']
    
    # تجهيز رسالة الواتساب المرتبة
    whatsapp_message = (
        f"🚨 *مقطع جديد جاهز للإمبراطورية يا قُصي!*\n\n"
        f"📌 *العنوان:*\n{title}\n\n"
        f"📝 *الوصف ورابط العمولة:*\n{description}\n\n"
        f"🖼️ *رابط الثمنيل (الصورة المصغرة):*\n{thumbnail}\n\n"
        f"🎬 *رابط تحميل الفيديو المباشر:*\n{video_url}"
    )
    
    send_to_whatsapp(whatsapp_message)

def send_to_whatsapp(message):
    # استخدام خدمة ويب هوك لإرسال الرسالة إلى واتسابك مباشرة
    # (يمكنك استبدال الرابط برقمك وخدمة الويب هوك المفضلة لديك مثل CallMeBot المجانية)
    phone_number = "YOUR_PHONE_NUMBER" # مثال: رقمك مع رمز الدولة
    api_key = "YOUR_API_KEY"
    
    url = f"https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={requests.utils.quote(message)}&apikey={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ تم إرسال الحزمة الكاملة إلى واتساب قُصي بنجاح!")
    else:
        print(f"❌ فشل الإرسال للواتساب: {response.status_code}")

if __name__ == "__main__":
    generate_qazo_content()
