import pygame

class Runner:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # إعداد المسارات (3 مسارات ثابتة)
        self.lanes = [screen_width // 4, screen_width // 2, (screen_width // 4) * 3]
        self.current_lane = 1  # البداية في المسار الأوسط
        
        # إعدادات الكائن (المؤشر _)
        self.x = self.lanes[self.current_lane]
        self.y = screen_height - 150
        self.width = 40
        self.height = 10
        
        self.color = (0, 255, 65) # أخضر حلوان
        self.speed = 5
        self.target_x = self.x # للتحريك السلس بين المسارات

    def move_left(self):
        if self.current_lane > 0:
            self.current_lane -= 1
            self.target_x = self.lanes[self.current_lane]

    def move_right(self):
        if self.current_lane < len(self.lanes) - 1:
            self.current_lane += 1
            self.target_x = self.lanes[self.current_lane]

    def update(self):
        # تحريك سلس (Interpolation) للمؤشر بين المسارات
        if self.x != self.target_x:
            diff = self.target_x - self.x
            self.x += diff * 0.2 # سرعة الانتقال الجانبي

    def draw(self, screen):
        # رسم المؤشر كخط وامض (مثل الطرفية)
        cursor_rect = pygame.Rect(self.x - self.width // 2, self.y, self.width, self.height)
        
        # إضافة تأثير الوميض (Blink) بناءً على الوقت
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            pygame.draw.rect(screen, self.color, cursor_rect)
