class CommandParser:
    def __init__(self):
        # خريطة الاختصارات لتسهيل اللعب السريع
        # تحويل الحروف البسيطة إلى أوامر نظام حلوان الكاملة
        self.aliases = {
            "i": "hpm i",
            "install": "hpm i",
            "u": "hpm u",
            "upgrade": "hpm u",
            "s": "hpm s",
            "refresh": "hpm s",
            "c": "clear",
            "cls": "clear",
            "n": "hel-netfix",
            "net": "hel-netfix"
        }

    def parse(self, raw_input):
        # 1. تنظيف النص (إزالة المسافات الزائدة وتحويله للأحرف الصغيرة)
        clean_input = raw_input.strip().lower()

        # 2. التحقق مما إذا كان المدخل عبارة عن اختصار (Alias)
        if clean_input in self.aliases:
            return self.aliases[clean_input]

        # 3. إذا لم يكن اختصاراً، نمرر الأمر كما هو (دعم للأوامر الكاملة)
        return clean_input

    def is_valid_syntax(self, command, available_commands):
        # التأكد من أن الأمر المكتوب موجود فعلياً في قاموس اللعبة
        return command in available_commands
