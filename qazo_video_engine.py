import requests

# رابط الـ Webhook الخاص بك في Make.com
WEBHOOK_URL = "https://hook.eu1.make.com/xv1z7yzllh6pcey2eiq2c4avmdqflff1"

def send_qazo_video():
    # بيانات الفيديو التجريبي برابط MP4 مباشر وسليم لمعالجته في يوتيوب
    payload = {
        "title": "Qazo Test Video - Fixed",
        "description": "هذا مقطع تجريبي حقيقي ومصحح لضمان المعالجة السليمة على يوتيوب.",
        "video_url": "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"
    }

    # إرسال البيانات إلى Make.com عبر الـ Webhook
    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("تم إرسال بيانات الفيديو بنجاح إلى Make.com وجاهز للرفع!")
    else:
        print(f"حدث خطأ في الإرسال: {response.status_code}")

if __name__ == "__main__":
    send_qazo_video()
