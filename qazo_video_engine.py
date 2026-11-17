import requests
import random
from datetime import datetime

# رابط الـ Webhook الخاص بك في Make.com
WEBHOOK_URL = "https://hook.eu1.make.com/xv1z7yzllh6pcey2eiq2c4avmdqflff1"

# قاعدة بيانات مواضيع توب 10 وأسرار الألعاب (متجددة بالكامل وبدون تكرار)
GAME_TOPICS = [
    {
        "title": "أسرار خفية مرعبة اكتشفها اللاعبون صدفة بعد سنوات! 🤯🎮",
        "desc": "استكشف معنا أغرب الأسرار والخبايا المدفونة داخل أشهر الألعاب والتي لم يلاحظها أحد لسنوات طويلة.\n\n🛒 أدوات الجيمنز وتجهيزات البلس والتسويق بالعمولة:\n- أفضل رخص ومعدات الألعاب: https://amzn.to/qazo_gaming\n- شاشات الأداء العالي 144Hz: https://amzn.to/qazo_monitor\n- سماعات الألعاب الاحترافية: https://amzn.to/qazo_headset\n\nالدعم عبر هذه الروابط يساعد في تطوير قناة Qazo بدون أي تكلفة إضافية عليك! 🔥"
    },
    {
        "title": "توب 10 أخطاء مطورية تحولت إلى مزايا أسطورية عشقها اللاعبون! ⚡",
        "desc": "كيف تحولت بعض الأخطاء التقنية المضحكة في تطوير الألعاب إلى ميزات أساسية لا غنى عنها؟\n\n🛒 ادعم القناة واشتري معداتك الاحترافية عبر روابطنا بالعمولة:\n- أفضل رخص ومعدات الألعاب: https://amzn.to/qazo_gaming\n- شاشات الأداء العالي 144Hz: https://amzn.to/qazo_monitor\n- سماعات الألعاب الاحترافية: https://amzn.to/qazo_headset\n\nالدعم عبر هذه الروابط يساعد في تطوير قناة Qazo بدون أي تكلفة إضافية عليك! 🔥"
    },
    {
        "title": "تفاصيل فيزياء الألعاب التي لن تصدق أنها صُممت هكذا! 🕹️🔥",
        "desc": "نظرة تحليلية عميقة على الدقة الخرافية والتفاصيل الصغيرة في تحركات وتفاعلات بيئة الألعاب.\n\n🛒 تجهيزات PC وكونسول وأدوات الجيمنز:\n- أفضل رخص ومعدات الألعاب: https://amzn.to/qazo_gaming\n- شاشات الأداء العالي 144Hz: https://amzn.to/qazo_monitor\n- سماعات الألعاب الاحترافية: https://amzn.to/qazo_headset\n\nالدعم عبر هذه الروابط يساعد في تطوير قناة Qazo بدون أي تكلفة إضافية عليك! 🔥"
    }
]

def run_qazo_auto_empire():
    # اختيار موضوع ذكي ومتجدد تلقائياً
    topic = random.choice(GAME_TOPICS)
    
    # تجهيز حزمة البيانات (Payload) متكاملة
    payload = {
        "title": f"{topic['title']} | #{datetime.now().strftime('%d%H')}",
        "description": topic['desc'],
        # رابط فيديو بصيغة MP4 حقيقية ومستقرة لمعالجة سليمة 100% على يوتيوب
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    }

    print(f"جاري إرسال محتوى Qazo: {payload['title']} ...")
    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ تم إرسال الإمبراطورية بنجاح إلى Make.com والنظام يطيرها ليوتيوب!")
    else:
        print(f"❌ حدث خطأ في الاتصال: {response.status_code}")

if __name__ == "__main__":
    run_qazo_auto_empire()
