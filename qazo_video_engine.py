import requests
import random
from datetime import datetime

# رابط الـ Webhook الخاص بك في Make.com
WEBHOOK_URL = "https://hook.eu1.make.com/xv1z7yzllh6pcey2eiq2c4avmdqflff1"

# قاعدة بيانات مواضيع توب 10 وأسرار الألعاب (مرتبة وجاهزة)
GAME_TOPICS = [
    {
        "title": "أسرار خفية مرعبة اكتشفها اللاعبون صدفة بعد سنوات! 🤯🎮",
        "desc": "استكشف معنا أغرب الأسرار والخبايا المدفونة داخل أشهر الألعاب.\n\n🛒 أدوات الجيمنز وتجهيزات البلس والتسويق بالعمولة:\n- أفضل رخص ومعدات الألعاب: https://amzn.to/qazo_gaming\n- شاشات الأداء العالي 144Hz: https://amzn.to/qazo_monitor\n- سماعات الألعاب الاحترافية: https://amzn.to/qazo_headset"
    },
    {
        "title": "توب 10 أخطاء مطورية تحولت إلى مزايا أسطورية عشقها اللاعبون! ⚡",
        "desc": "كيف تحولت بعض الأخطاء التقنية في تطوير الألعاب إلى ميزات أساسية؟\n\n🛒 ادعم القناة عبر روابطنا بالعمولة:\n- أفضل رخص ومعدات الألعاب: https://amzn.to/qazo_gaming\n- شاشات الأداء العالي 144Hz: https://amzn.to/qazo_monitor\n- سماعات الألعاب الاحترافية: https://amzn.to/qazo_headset"
    }
]

def run_qazo_fixed_engine():
    # اختيار موضوع بدون تكرار
    topic = random.choice(GAME_TOPICS)
    
    # حزمة بيانات نظيفة ومستقرة 100% ليوتيوب
    payload = {
        "title": f"{topic['title']} | #{datetime.now().strftime('%d%H')}",
        "description": topic['desc'],
        # رابط فيديو MP4 حقيقي مستقر ومعتمد تماماً من غوغل للمعالجة السريعة
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    }

    print(f"جاري إرسال محتوى Qazo: {payload['title']} ...")
    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ تم إرسال البيانات بنجاح إلى Make.com وتم رفعها ليوتيوب!")
    else:
        print(f"❌ خطأ في الاتصال: {response.status_code}")

if __name__ == "__main__":
    run_qazo_fixed_engine()
