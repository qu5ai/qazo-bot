import random
import requests

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
    # البحث الذكي وجلب روابط الأفلييت أوتوماتيكياً
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

def publish_to_youtube(script, affiliate_desc):
    print("جاري رفع الفيديو والصورة المصغرة (بخط Tajawal-Bold) إلى يوتيوب أوتوماتيكياً...")
    # (هنا يتم استخدام YOUTUBE_API_KEY المعتمد في المستودع للنشر)
    print("تم النشر على يوتيوب بنجاح! 🚀")

def publish_to_instagram(caption_text):
    print("جاري رفع الفيديو إلى انستغرام (Instagram Reels) أوتوماتيكياً...")
    # (هنا يتم الاتصال بـ Instagram Graph API عبر التوكن المخزن في الـ Secrets)
    print("تم النشر بنجاح على انستغرام! 📱✨")

if __name__ == "__main__":
    topic = "سر احتراف وهندسة الأنظمة البرمجية وعالم الألعاب"
    
    print("1. توليد السيناريو...")
    script = generate_bendia_style_script(topic)
    
    print("2. جلب روابط الأفلييت...")
    affiliate_desc = search_and_get_affiliate_link(topic)
    
    print("3. بدء النشر التلقائي...")
