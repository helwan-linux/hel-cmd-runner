import pygame
import random

class VisualEffects:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.flash_timer = 0
        self.flash_color = (0, 255, 65)
        self.shake_amount = 0

    def trigger_success_flash(self):
        self.flash_timer = 10
        self.flash_color = (0, 100, 0) # أخضر غامق للنجاح

    def trigger_error_shake(self):
        self.flash_timer = 15
        self.flash_color = (100, 0, 0) # أحمر للخطأ
        self.shake_amount = 10

    def apply_effects(self, screen):
        # 1. تأثير الوميض (Flash)
        if self.flash_timer > 0:
            overlay = pygame.Surface((self.width, self.height))
            overlay.set_alpha(self.flash_timer * 10)
            overlay.fill(self.flash_color)
            screen.blit(overlay, (0, 0))
            self.flash_timer -= 1

        # 2. تأثير الاهتزاز (Screen Shake)
        shake_offset = (0, 0)
        if self.shake_amount > 0:
            shake_offset = (random.randint(-self.shake_amount, self.shake_amount),
                            random.randint(-self.shake_amount, self.shake_amount))
            self.shake_amount -= 1
        return shake_offset

    def draw_glitch(self, screen):
        # رسم خطوط "نويز" بسيطة تعطي إيحاء الطرفية القديمة
        for _ in range(3):
            y = random.randint(0, self.height)
            pygame.draw.line(screen, (0, 50, 0), (0, y), (self.width, y), 1)
