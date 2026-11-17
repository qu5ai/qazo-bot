import random
import requests
import json

def generate_bendia_style_script(topic):
    # مولد السيناريو بأسلوب بنديا (مقدمة خاطفة، سرد تحليلي، وخاتمة تترك أثراً)
    hooks = [
        f"تخيل معي لو أن كل ما تعرفه عن {topic} كان مجرد قمة الجبل... اليوم سنغوص في العمق ونكتشف الحقيقة الكاملة.",
        f"لماذا يفشل الجميع في فهم الحقيقة خلف {topic}؟ السر أبسط وأغرب مما تتخيل بكثير.",
        f"في لحظة واحدة، كل القواعد التي نعرفها عن {topic} تغيرت للأبد. دعونا نكتشف القصة الحقيقية."
    ]
    
    selected_hook = random.choice(hooks)
    
    script = f"""
    [المقدمة - الخاطفة]:
    {selected_hook}
    
    [صلب الموضوع - السرد والتحليل العميق]:
    - النظرة السطحية للأمور عادة ما تخدعنا، لكن عندما نحلل ما يجري خلف الكواليس في عالم {topic}، نجد أن التفاصيل الدقيقة هي التي تصنع الفارق الحقيقي.
    - تماماً مثل محترف يقرأ حركة الخصم قبل أن تنفذ، البناء الصحيح يبدأ من تفكيك المشكلة إلى أجزائها البسيطة ثم إعادة تركيبها بطريقة ذكية ومتكاملة.
    
    [الخاتمة - التساؤل المفتوح]:
    والسؤال الآن، هل أنت مستعد لتغيير منظورك بالكامل؟ شاركني رأيك في التعليقات، ولا تنسَ الاشتراك لتبقى في قلب الحدث مع Qazo.
    """
    return script.strip()

def search_and_get_affiliate_link(video_topic):
    # البحث الذكي وجلب روابط الأفلييت أوتوماتيكياً حسب المحتوى
    affiliate_database = {
        "gaming": "https://amzn.to/qazo-gaming-pc-setup",
        "programming": "https://amzn.to/qazo-dev-tools",
        "general": "https://amzn.to/qazo-store"
    }
    
    topic_lower = video_topic.lower()
    if "برمجة" in topic_lower or "كود" in topic_lower or "python" in topic_lower:
        selected_link = affiliate_database["programming"]
        category_name = "أدوات وتطبيقات المطورين البرمجية"
    elif "لعبة" in topic_lower or "جيمنج" in topic_lower or "pc" in topic_lower or "تجميعة" in topic_lower:
        selected_link = affiliate_database["gaming"]
        category_name = "عتاد التجميعات وأجهزة الألعاب"
    else:
        selected_link = affiliate_database["general"]
        category_name = "متجر Qazo الشامل"
        
    affiliate_block = f"""
    --------------------------------------------------
    🔥 الدعم والتسويق بالعمولة (روابط موصى بها من Qazo):
    - {category_name}: {selected_link}
    (الدعم عبر هذه الروابط يساعد في تطوير قناة Qazo بدون أي تكلفة إضافية عليك!)
    --------------------------------------------------
    """
    return affiliate_block

def send_to_cloud_automation(video_data):
    # تم إدراج رابط الويب هوك الخاص بك هنا بشكل رسمي
    webhook_url = "https://hook.eu1.make.com/xv1z7yzllh6pcey2eiq2c4avmdqflff1"
    
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(webhook_url, data=json.dumps(video_data), headers=headers)
        if response.status_code == 200:
            print("✨ تم إرسال حزمة بيانات Qazo إلى Make.com بنجاح!")
        else:
            print(f"فشل الإرسال، رمز الاستجابة: {response.status_code}")
    except Exception as e:
        print(f"خطأ في الاتصال بالأداة السحابية: {e}")

if __name__ == "__main__":
    topic = "سر احتراف وهندسة الأنظمة البرمجية وعالم الألعاب"
    
    print("1. توليد السيناريو أوتوماتيكياً...")
    script = generate_bendia_style_script(topic)
    
    print("2. جلب روابط الأفلييت الذكية...")
    affiliate_desc = search_and_get_affiliate_link(topic)
    
    # تجهيز حزمة البيانات وإرسالها للمنصات عبر Make.com
    qazo_package = {
        "title": topic,
        "script": script,
        "affiliate_link": affiliate_desc,
        "video_file_url": "https://github.com/your-username/qazo-repo/raw/main/output_video.mp4"
    }
    
    send_to_cloud_automation(qazo_package)
    print("✨ تمت عملية الإنتاج والإرسال السحابي بالكامل!")
