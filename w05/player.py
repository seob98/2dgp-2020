import random
from pico2d import *
import gfw
import gfw_image
from gobj import *

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 100, 100
        self.delta = 0, 0
        self.speed = 0
        self.image = gfw_image.load(RES_DIR + '/fighter.png')

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        self.pos = point_add(self.pos, self.delta)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.delta = point_add(self.delta, Player.KEY_MAP[pair])
