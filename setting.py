import os
import pygame as pg

setting = {
    'w': 800,
    'h': 800,
    'title': 'Test',
    'fps': 60,
}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')



game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')

obst = pg.image.load(os.path.join(media_folder, 'ObstacleDenis.png'))
player_img = pg.image.load(os.path.join(media_folder, 'player.png'))
