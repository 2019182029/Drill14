from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        sx, sy = self.x - server.boy.bg.window_left, self.y - server.boy.bg.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        sx, sy = self.x - server.boy.bg.window_left, self.y - server.boy.bg.window_bottom
        # return self.x - 10, self.y - 10, self.x + 10, self.y + 10
        return sx - 10, sy - 10, sx + 10, sy + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                other.ball = self # 소년이 볼을 소유하도록.
                game_world.remove_object(self)
            case 'zombie:ball':
                other.ball = self