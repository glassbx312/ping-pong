from pygame import *
import json
import os

settings = {
    "fullscreen": False,
    "resolution": (800, 600),
    "difficulty": "easy",
    "host": "127.0.0.1",
    "port": 8080,
}

if os.path.exists('settings.json'):
    with open('settings.json', 'r') as file:
        settings = json.load(file)
        fullscreen = settings["fullscreen"]
        resolution = settings["resolution"]
        difficulty = settings["difficulty"]
        host = settings["host"]
        port = settings["port"]
else:
    with open('settings.json', 'w') as file:
        json.dump(settings, file)
        fullscreen = settings["fullscreen"]
        resolution = settings["resolution"]
        difficulty = settings["difficulty"]
        host = settings["host"]
        port = settings["port"]

#кольори
BG_COLOR = (100, 0, 99)
BTN_COLOR = (16, 1, 95)
BTN_HOVER_COLOR = (40, 0, 100)
#шрифти
font.init()
font1 = font.Font("fonts\Minecraft_1.0.ttf", 30)

difficulty_game = ["easy", "normal", "hard"]

window = display.set_mode(resolution, FULLSCREEN if fullscreen else RESIZABLE)
display.set_caption("Меню")
clock = time.Clock()

class Button:
    def __init__(self, text, font, size, gap, color, hover_color):
        self.text = text
        self.font = font
        self.size = size
        self.gap = gap
        self.color = color
        self.hover_color = hover_color
        self.rect = Rect(0, 1, size[0], size[1])
        self.rect.center = (resolution[0] // 2, resolution[1] // 2 + gap)

    def draw(self, screen):
        if self.rect.collidepoint(mouse.get_pos()):
            btn_color = self.hover_color
        else:
            btn_color = self.color
        draw.rect(screen, btn_color, self.rect)
        text_surface = self.font.render(self.text, True, (254, 255,255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, events):
        return events.type == MOUSEBUTTONDOWN and self.rect.collidepoint(events.pos)

def menu_loop():
    new_game_btn = Button("Нова Гра", font1, [400, 40], -50, BTN_COLOR, BTN_HOVER_COLOR)
    settings_btn = Button("Налаштування", font1, [400, 40], 0, BTN_COLOR, BTN_HOVER_COLOR)
    exit_btn = Button("Вийти", font1, [400, 40], 50, BTN_COLOR, BTN_HOVER_COLOR)

    game = True
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
            if exit_btn.is_clicked(e):
                game = False
            if settings_btn.is_clicked(e):
                game = False
                settings_menu_loop()


        window.fill(BG_COLOR)
        new_game_btn.draw(window)
        settings_btn.draw(window)
        exit_btn.draw(window)

        display.update()
        clock.tick(60)

def settings_menu_loop():
    global fullscreen, resolution, difficulty, host, port
    back_btn = Button("Назад", font1, [400, 40], -100, BTN_COLOR, BTN_HOVER_COLOR)
    fullscreen_btn = Button(f"повний екран:{fullscreen}", font1, [400, 40], -50, BTN_COLOR, BTN_HOVER_COLOR)
    difficulty_btn = Button(f"складність:{difficulty}", font1, [400, 40], 0, BTN_COLOR, BTN_HOVER_COLOR)
    host_btn = Button(f"host: {host} ", font1, [400, 40], 50, BTN_COLOR, BTN_HOVER_COLOR)
    port_btn = Button(f"port: {port}", font1, [400, 40], 100, BTN_COLOR, BTN_HOVER_COLOR)

    game = True
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
            if back_btn.is_clicked(e):
                game = False
                menu_loop()
            if fullscreen_btn.is_clicked(e):
                fullscreen_btn.text = f"повний екран:{fullscreen}"
                fullscreen = not fullscreen
                with open("settings.json", "w") as file:
                    settings["fullscreen"] = fullscreen
                    json.dump(settings, file)
            if difficulty_btn.is_clicked(e):
                difficulty_id = difficulty_game.index(difficulty) + 1 if difficulty_game.index(difficulty) < len(difficulty_game) - 1 else 0
                difficulty = difficulty_game[difficulty_id]
                difficulty_btn.text = f"складність:{difficulty}"
                with open("settings.json", "w") as file:
                    settings["difficulty"] = difficulty
                    json.dump(settings, file)

        window.fill(BG_COLOR)
        back_btn.draw(window)
        fullscreen_btn.draw(window)
        difficulty_btn.draw(window)
        host_btn.draw(window)
        port_btn.draw(window)

        display.update()
        clock.tick(60)

menu_loop()