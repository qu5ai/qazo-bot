import requests
import urllib.parse

def search_and_get_affiliate_link(video_topic):
    # محاكاة محرك البحث الذكي للبحث عن برامج أفلييت مرتبطة بموضوع الفيديو
    # (يمكننا ربطه بمصادر أو قواعد بيانات جاهزة للروابط حسب نيش قناتك)
    print(f"جاري البحث عن برامج أفلييت مناسبة لموضوع: {video_topic} ...")
    
    # أمثلة لقواعد بيانات روابط أفلييت مقسمة حسب النيش (Gaming / Programming)
    affiliate_database = {
        "gaming": "https://amzn.to/qazo-gaming-pc-setup",
        "programming": "https://amzn.to/qazo-dev-tools",
        "general": "https://amzn.to/qazo-store"
    }
    
    # تحديد النيش بناءً على عنوان الفيديو أوتوماتيكياً
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
        
    # بناء نص الوصف التسويقي أوتوماتيكياً بالكامل
    affiliate_block = f"""
    --------------------------------------------------
    🔥 الدعم والتسويق بالعمولة (روابط موصى بها من Qazo):
    - {category_name}: {selected_link}
    (الدعم عبر هذه الروابط يساعد في تطوير قناة Qazo بدون أي تكلفة إضافية عليك!)
    --------------------------------------------------
    """
    return affiliate_block

if __name__ == "__main__":
    # تجربة البحث والدمج التلقائي
    topic = "كيف تحترف برمجة الألعاب وتحسين أداء كود بايثون"
    print(search_and_get_affiliate_link(topic))
