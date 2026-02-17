import pygame
import random

class Obstacle:
    def __init__(self, x, y, is_command=False, command_text=""):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 40
        self.is_command = is_command
        self.command_text = command_text
        self.active = True

class Track:
    def __init__(self, screen_width, screen_height, lanes):
        self.width = screen_width
        self.height = screen_height
        self.lanes = lanes
        self.obstacles = []
        self.speed = 2
        self.font = pygame.font.SysFont("monospace", 18, bold=True)

    def update(self):
        # إضافة عقبات جديدة بشكل عشوائي
        if random.random() < 0.02:
            lane = random.choice(self.lanes)
            # 50% عقبة عادية و 50% عقبة برمجية
            is_cmd = random.random() > 0.5
            cmd_text = ""
            if is_cmd:
                # اختيار أمر عشوائي من أوامر حلوان [cite: 2026-01-28]
                cmd_text = random.choice(["hpm i", "hpm u", "clear", "hel-netfix"])
            
            self.obstacles.append(Obstacle(lane, -50, is_cmd, cmd_text))

        # تحريك العقبات وحذف الخارجة عن الشاشة
        for obs in self.obstacles:
            obs.y += self.speed
        self.obstacles = [obs for obs in self.obstacles if obs.y < self.height]

    def draw(self, screen):
        for obs in self.obstacles:
            if not obs.active:
                continue
            
            # لون العقبة: أحمر للأوامر، رمادي للحواجز
            color = (200, 0, 0) if obs.is_command else (100, 100, 100)
            pygame.draw.rect(screen, color, (obs.x - obs.width//2, obs.y, obs.width, obs.height))

            # أهم جزء: كتابة الأمر فوق العقبة عشان المستخدم يشوفه [cite: 2026-02-17]
            if obs.is_command:
                text_surf = self.font.render(obs.command_text, True, (255, 255, 255))
                screen.blit(text_surf, (obs.x - obs.width//2, obs.y - 25))
