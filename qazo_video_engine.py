import os
import random
from PIL import Image, ImageDraw, ImageFont

class QazoVisualEngine:
    def __init__(self):
        self.brand_name = "Qazo"
        print(f"[{self.brand_name}] تهيئة محرك الإبهار البصري للشخصية والعناوين التفاعلية...")

    def generate_scene_frame(self, title_text, scene_description, output_filename="scene_output.png"):
        """
        يقوم بتوليد إطار الفيديو لكل فقرة:
        1. شريط علوي أبيض نظيف يحمل العنوان (مثل: التحليلي، القيادي، المسالم).
        2. خلفية تفاعلية تعبر عن محتوى الشرح.
        3. تمثيل للشخصية الكرتونية Qazo وهي تتفاعل في المقدمة.
        """
        # إنشاء لوحة فيديو أبعاد قصيرة (YouTube Shorts / TikTok - 1080x1920)
        width, height = 1080, 1920
        img = Image.new("RGB", (width, height), color=(245, 245, 245))
        draw = ImageDraw.Draw(img)

        # 1. تصميم الشريط العلوي للعنوان (أبيض ناصع مع حدود أنيقة)
        header_height = 200
        draw.rectangle([0, 0, width, header_height], fill=(255, 255, 255), outline=(200, 200, 200), width=3)
        
        # رسم العنوان العلوي (يمكن ربطه ب خط عربي مدعوم في بيئة السيرفر)
        # ملاحظة: يتم تمرير العنوان مثل "التحليلي" أو "القيادي" ديناميكياً
        draw.text((width // 2 - 150, 70), title_text, fill=(20, 20, 20))

        # 2. رسم مساحة الخلفية التفاعلية خلف الشخصية
        bg_box = [50, 250, width - 50, 1100]
        draw.rectangle(bg_box, fill=(230, 240, 250), outline=(180, 200, 220), width=2)
        draw.text((80, 300), f"خلفية تفاعلية: {scene_description}", fill=(50, 50, 50))

        # 3. محاكاة وضعية الشخصية الكرتونية Qazo في الواجهة الأمامية
        # الشخصية تتحرك، تشرح، وتتفاعل بحركات يمين ويسار
        character_box = [150, 1150, 930, 1850]
        draw.rounded_rectangle(character_box, radius=30, fill=(255, 255, 255), outline=(50, 50, 50), width=5)
        draw.text((200, 1250), "🤖 [ QAZO Character ]", fill=(10, 10, 10))
        draw.text((200, 1320), "أنا أتفاعل وأشرح هنا...", fill=(100, 100, 100))

        # حفظ الإطار الناتج
        img.save(output_filename)
        print(f"[{self.brand_name}] تم بنجاح إنشاء إطار المشهد: {output_filename}")
        return output_filename

    def build_autonomous_episode(self, script_scenes):
        """
        يبني حلقة متكاملة من عدة مشاهد يتم توليدها أوتوماتيكياً
        """
        print(f"[{self.brand_name}] بدء بناء الفيديو الأوتوماتيكي بالكامل...")
        generated_frames = []
        
        for index, scene in enumerate(script_scenes):
            title = scene.get("title", "عام")
            desc = scene.get("description", "شرح تفصيلي")
            filename = f"frame_{index+1}.png"
            
            frame_path = self.generate_scene_frame(title, desc, filename)
            generated_frames.append(frame_path)
            
        print(f"[{self.brand_name}] اكتمل توليد كافة إطارات الحلقة بنجاح وجاهزة للدمج والرفع!")
        return generated_frames

if __name__ == "__main__":
    # تجربة تشغيل محرك Qazo البصري محلياً أو عبر السيرفر
    engine = QazoVisualEngine()
    
    # نموذج لسيناريو مقسم لفقرات مع عناوينها العلوية
    sample_script = [
        {"title": "التعريفي", "description": "مقدمة إمبراطورية قازو الجديدة"},
        {"title": "التحليلي", "description": "استعراض تفاصيل اللعب والأسرار الخفية"},
        {"title": "القيادي", "description": "خطوات الاحتراف الحقيقي وكيف تتجاوز المنافسين"}
    ]
    
    engine.build_autonomous_episode(sample_script)
