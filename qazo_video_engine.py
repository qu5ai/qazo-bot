import requests
import random
from datetime import datetime

WEBHOOK_URL = "https://hook.eu1.make.com/xv1z7yzllh6pcey2eiq2c4avmdqflff1"

# قائمة المواضيع الضخمة (توب 10 وأسرار خفية للألعاب) لتجنب التكرار
TOPICS_POOL = [
    {
        "title": "أسرار خفية مرعبة اكتشفها اللاعبون بعد سنوات من صدور اللعبة! 🎮🔥",
        "desc": "استكشف معنا أغرب الأسرار والخبايا المدفونة داخل أشهر الألعاب والتي لمჩلاحظها أحد.\n\n🛒 أدوات الجيمنز وتجهيزات البلس:\n- أفضل رخص ومعدات الألعاب: https://amzn.to/qazo_gaming\n- كيبورد وماوس الأداء العالي: https://amzn.to/qazo_gear",
    },
    {
        "title": "توب 10 أخطاء مطورية أدت إلى مزايا أسطورية غير متوقعة! 🤯",
        "desc": "كيف تحولت بعض الأخطاء التقنية في تطوير الألعاب إلى ميزات عشقها ملايين اللاعبين حول العالم؟\n\n🛒 ادعم القناة واشتري معداتك عبر روابطنا بالعمولة:\n- شاشات الأداء العالي 144Hz: https://amzn.to/qazo_monitor\n- سماعات الألعاب الاحترافية: https://amzn.to/qazo_headset",
    },
    {
        "title": "أعظم تفاصيل الفيزياء في الألعاب التي لن تصدق أنها موجودة! ⚡",
        "desc": "نظرة تحليلية عميقة على الدقة الخرافية في تفاعلات بيئة اللعب وفيزياء الحركة.\n\n🛒 تجهيزات PC وكونسول:\n- قطع الـ PC الموصى بها: https://amzn.to/qazo_pc",
    }
]

def generate_qazo_post():
    # اختيار موضوع عشوائي لضمان عدم التكرار نهائياً
    selected_topic = random.choice(TOPICS_POOL)
    
    payload = {
        "title": f"{selected_topic['title']} - #{datetime.now().strftime('%d%H%M')}",
        "description": selected_topic['desc'],
        # رابط فيديو تجريبي مستقر (يمكن استبداله لاحقاً بالفيديو المنتج آلياً)
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    }

    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print("تم إرسال محتوى Qazo بنجاح إلى Make.com والنظام يجهز النشر!")
    else:
        print(f"خطأ في الإرسال: {response.status_code}")

if __name__ == "__main__":
    generate_qazo_post()
