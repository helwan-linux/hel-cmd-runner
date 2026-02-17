import pygame
import sys
from engine.runner import Runner
from engine.track import Track
from engine.collision import CollisionSystem
from ui.terminal import TerminalUI
from ui.effects import VisualEffects
from logic.commands import CommandActions
from logic.state import GameState
from logic.parser import CommandParser

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

def show_tutorial_menu(screen, font):
    screen.fill((5, 5, 5))
    
    # العناوين الرئيسية
    title = font.render("HELWAN COMMAND RUNNER", True, (0, 255, 65))
    screen.blit(title, (SCREEN_WIDTH//2 - 180, 50))

    # --- شرح "إزاي تلعب" (الكتالوج اللي اتفقنا عليه) ---
    y_offset = 150
    instructions = [
        ("1. USE ARROWS:", (255, 255, 255)),
        ("   To MOVE and AVOID Grey Blocks (Death).", (200, 200, 200)),
        ("", (0,0,0)),
        ("2. USE KEYBOARD:", (255, 255, 255)),
        ("   Type the command above RED blocks + ENTER to destroy them.", (200, 200, 200)),
        ("", (0,0,0)),
        ("3. SHORTCUTS (Fast Score):", (0, 255, 65)),
        ("   'i' = install | 'c' = clear | 'n' = netfix | 'u' = upgrade", (0, 255, 65)),
        ("", (0,0,0)),
        ("PRESS [ SPACE ] TO START PLAYING", (255, 255, 0)),
        ("PRESS [ Q ] TO QUIT", (255, 0, 0))
    ]

    for text, color in instructions:
        line = font.render(text, True, color)
        screen.blit(line, (100, y_offset))
        y_offset += 35

    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # هنا كان فيه علامة تنصيص ناقصة وقوس مقفولش
    pygame.display.set_caption("Helwan Command Runner") 
    
    try:
        # تأكد إن فولدر images جنبه ملف main.py وجواه icon.png
        icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(icon)
    except:
        # لو فشل مش هيعطل اللعبة بس الأيقونة مش هتظهر
        pass
        
    font_main = pygame.font.SysFont("monospace", 20, bold=True)
    clock = pygame.time.Clock()

    while True:
        # شاشة التعليمات الإجبارية قبل أي لعب
        in_menu = True
        while in_menu:
            show_tutorial_menu(screen, font_main)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: in_menu = False
                    if event.key == pygame.K_q: pygame.quit(); sys.exit()

        # إعدادات اللعبة
        runner = Runner(SCREEN_WIDTH, SCREEN_HEIGHT)
        state = GameState()
        track = Track(SCREEN_WIDTH, SCREEN_HEIGHT, runner.lanes)
        terminal = TerminalUI(SCREEN_WIDTH, SCREEN_HEIGHT)
        collision_sys = CollisionSystem()
        parser = CommandParser()
        effects = VisualEffects(SCREEN_WIDTH, SCREEN_HEIGHT)
        cmd_actions = CommandActions(state)
        
        game_active = True
        feedback_msg = "GO! AVOID GREY | DESTROY RED"

        while game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: pygame.quit(); sys.exit()
                    if event.key == pygame.K_LEFT: runner.move_left()
                    if event.key == pygame.K_RIGHT: runner.move_right()

                raw_cmd = terminal.update_input(event)
                if raw_cmd:
                    cmd = parser.parse(raw_cmd)
                    if collision_sys.check_command_hit(cmd, track.obstacles, runner):
                        state.update_score(200)
                        feedback_msg = f"SUCCESS: {cmd} (+200)"
                        effects.trigger_success_flash()
                    else:
                        feedback_msg = "WRONG COMMAND!"
                        effects.trigger_error_shake()

            runner.update()
            track.update()
            track.speed = state.current_speed
            state.update_score(1)

            if collision_sys.check_physical_collision(runner, track.obstacles):
                game_active = False

            screen.fill((5, 5, 5))
            track.draw(screen)
            runner.draw(screen)
            terminal.draw_input_bar(screen)
            terminal.draw_feedback(screen, feedback_msg)
            
            # السكور المباشر
            score_txt = font_main.render(f"SCORE: {state.score}", True, (0, 255, 65))
            screen.blit(score_txt, (20, 20))
            
            pygame.display.flip()
            clock.tick(60)

        # شاشة النهاية وخيار الإعادة
        in_game_over = True
        while in_game_over:
            screen.fill((30, 0, 0))
            over_txt = font_main.render(f"GAME OVER! YOUR SCORE: {state.score}", True, (255, 255, 255))
            retry_txt = font_main.render("PRESS [ R ] TO RESTART OR [ Q ] TO QUIT", True, (0, 255, 65))
            screen.blit(over_txt, (SCREEN_WIDTH//2 - 180, SCREEN_HEIGHT//2 - 20))
            screen.blit(retry_txt, (SCREEN_WIDTH//2 - 220, SCREEN_HEIGHT//2 + 40))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: in_game_over = False
                    if event.key == pygame.K_q: pygame.quit(); sys.exit()

if __name__ == "__main__":
    main()
