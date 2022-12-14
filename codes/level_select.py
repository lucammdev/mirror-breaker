import pygame
from button import Button


class LevelSelect():
    def __init__(self, surface, create_level, create_menu, max_level):

        self.display_surface = surface
        self.background = pygame.image.load('assets/menusBackground.png').convert_alpha()

        self.buttons = pygame.sprite.Group()

        self.max_level = max_level

        self.create_level_buttons(max_level, create_level)

        self.create_menu = create_menu




    def create_level_buttons(self, level_achieved, create_level):
        for i in range(level_achieved+1):
            string = str(i+1)
            if i < 4:
                self.buttons.add(Button('assets/button/level'+string+'Button_fade.png','assets/button/level'+string+'Button_full.png',(60 + i*(300), 60), create_level, i))
            elif i < 8:
                self.buttons.add(Button('assets/button/level'+string+'Button_fade.png','assets/button/level'+string+'Button_full.png',(60 + (i%4)*(300), 260), create_level, i))
            elif i < 12:
                self.buttons.add(Button('assets/button/level'+string+'Button_fade.png','assets/button/level'+string+'Button_full.png',(60 + (i%4)*(300), 460), create_level, i))


    def input_return(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu(self.max_level)

    def run(self):
        self.display_surface.blit(self.background,(-105,0))
        self.buttons.draw(self.display_surface)
        self.buttons.update()
        self.input_return()
