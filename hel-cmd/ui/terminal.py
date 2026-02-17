import pygame

class TerminalUI:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.bg_color = (10, 10, 10)
        self.text_color = (0, 255, 65) # لون حلوان الأخضر المميز
        self.font = pygame.font.SysFont("monospace", 22)
        self.input_text = ""
        self.prompt = "helwan@user:~$ "

    def draw_input_bar(self, screen):
        # رسم خلفية الطرفية في أسفل الشاشة
        pygame.draw.rect(screen, (20, 20, 20), (0, self.height - 70, self.width, 70))
        pygame.draw.line(screen, self.text_color, (0, self.height - 70), (self.width, self.height - 70), 2)

        # سطر المساعدة للمستخدم (التلميحات)
        help_text = "HINT: i=install, c=clear, n=netfix, u=upgrade"
        help_surf = self.font.render(help_text, True, (80, 80, 80))
        screen.blit(help_surf, (10, self.height - 95))

        # رسم النص الذي يكتبه اللاعب حالياً
        display_text = self.prompt + self.input_text
        text_surface = self.font.render(display_text, True, self.text_color)
        screen.blit(text_surface, (10, self.height - 50))

    def update_input(self, event):
        # معالجة مفاتيح الكتابة
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                command_to_send = self.input_text
                self.input_text = ""
                return command_to_send
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode
        return None

    def draw_feedback(self, screen, message):
        # رسم رسائل النظام (مثل SUCCESS أو ERROR)
        if message:
            feedback_surface = self.font.render(f"[*] {message}", True, (255, 255, 255))
            screen.blit(feedback_surface, (10, self.height - 120))
