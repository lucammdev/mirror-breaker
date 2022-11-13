import pygame

from player import Player
from setting import *
from tiles import Tile
from setting import level_maps

class Level:
    def __init__(self, surface, create_menu, create_level, level_number):
        # level set_up
        self.display_surface = surface
        self.background = pygame.image.load('assets/background.jpg').convert_alpha()
        self.create_menu = create_menu # Depois usar para retornar ao menu
        self.create_level = create_level # Depois usar quando terminar a fase para poder ir para proxima
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()  # sempre cria um grupo (mesmo que solitário) e depois instancia e  adiciona
        self.world_shift = 0
        self.level_number = level_number#Next level seria isso + 1
        self.setup_level(level_maps[level_number])  # pode já executar uma função quando instancia ISSO TEM QUE SER SEMPRE NO FINAL
        # pois pode dar problema com o que vier antes

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'x' or cell == 'X':
                    for i in range(2):
                        for j in range(2):
                            tile = Tile((col_index * tile_size + i*28, row_index * tile_size + j*28))
                            self.tiles.add(tile)
                elif cell == 'P':
                    player_sprite = Player((col_index * tile_size, row_index * tile_size ))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/5 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width*4/5 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():  #todo adicionar wallJUmp
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0: # melhor forma de ver com o que se está colidindo
                    player.rect.top = sprite.rect.bottom
                    player.reset_vertical_momentum()
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.can_jump = True
                    player.reset_vertical_momentum()
    

    def input_return(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu(self.level_number)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        player.gravity = 0.8
        player.can_wall_jump = False

        for sprite in self.tiles.sprites(): #todo consertar walljump após saber usar temporizador
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: # melhor forma de ver com o que se está colidindo
                    player.rect.left = sprite.rect.right
                    self.vertical_movement_collision()
                    player.gravity = 0.3
                    player.reset_vertical_momentum()
                    player.can_wall_jump = True
                    player.wall_jump_direction = 6
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.vertical_movement_collision()
                    player.gravity = 0.3
                    player.reset_vertical_momentum()
                    player.can_wall_jump = True
                    player.wall_jump_direction = -6


    def player_movement(self):
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

    def run(self):
        self.display_surface.blit(self.background,(0,0))
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.player_movement()
        self.player.draw(self.display_surface)

        self.input_return()

