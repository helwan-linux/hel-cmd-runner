import pygame

class Assets:
    def __init__(self):
        # تحميل الخطوط - نستخدم Monospace لتعزيز شكل الطرفية
        try:
            self.font_main = pygame.font.SysFont("monospace", 22, bold=True)
            self.font_small = pygame.font.SysFont("monospace", 16)
        except:
            self.font_main = pygame.font.Font(None, 24)
            self.font_small = pygame.font.Font(None, 18)

    def get_ascii_art(self, type):
        # فن ASCII للعقبات ليعطي طابع Linux القديم
        arts = {
            "firewall": [
                "[ #### ]",
                "[ FIRE ]",
                "[ WALL ]"
            ],
            "zombie": [
                "< ZOMBIE >",
                "  (pid)  "
            ],
            "kernel_err": [
                "!! KERNEL !!",
                "!! ERROR  !!"
            ]
        }
        return arts.get(type, ["[ ERROR ]"])

    def draw_ascii_obstacle(self, screen, x, y, art_type, color=(0, 255, 65)):
        art = self.get_ascii_art(art_type)
        for i, line in enumerate(art):
            text_surf = self.font_small.render(line, True, color)
            screen.blit(text_surf, (x - 40, y + (i * 15)))
