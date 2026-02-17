import pygame

class CollisionSystem:
    def __init__(self):
        pass

    def check_command_hit(self, command_text, obstacles, runner):
        # البحث عن العقبات البرمجية التي تطابق النص المكتوب
        for obs in obstacles:
            if obs.is_command and obs.active:
                if obs.command_text == command_text:
                    obs.active = False # تعطيل العقبة فوراً [cite: 2026-02-17]
                    return True
        return False

    def check_physical_collision(self, runner, obstacles):
        # فحص التصادم الجسدي بين اللاعب والعقبات النشطة فقط
        runner_rect = pygame.Rect(runner.x - runner.width // 2, runner.y, runner.width, runner.height)
        
        for obs in obstacles:
            if obs.active: # لو العقبة لسه موجودة (ماتمسحتش بكود) [cite: 2026-02-17]
                obs_rect = pygame.Rect(obs.x - obs.width // 2, obs.y, obs.width, obs.height)
                if runner_rect.colliderect(obs_rect):
                    return True # حدث تصادم حقيقي [cite: 2026-02-17]
        return False
