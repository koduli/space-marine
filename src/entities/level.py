from src.entities.block import Block
from src.entities.fire import Fire
from src.entities.player import Player
from src.config.settings import HEIGHT, WIDTH

class Level:
    def __init__(self):
        self.block_size = 96
        self.player = Player(100, HEIGHT - self.block_size - 64, 32, 32)
        self.objects = self.create_level()

    def create_floor(self):
        return [Block(i * self.block_size, HEIGHT - self.block_size + 2, self.block_size)
                for i in range(-WIDTH // self.block_size, (WIDTH * 2) // self.block_size)]

    def create_blocks(self):
        return [
            Block(0, HEIGHT - self.block_size * 2 + 5, self.block_size),
            Block(300, 305, self.block_size),
            Block(570, HEIGHT - self.block_size * 2 + 5, self.block_size),
            Block(666, HEIGHT - self.block_size * 2 + 5, self.block_size),
            Block(666, HEIGHT - self.block_size * 3 + 8, self.block_size),
            Block(1200, HEIGHT - self.block_size * 2 + 5, self.block_size),
            Block(1200, HEIGHT - self.block_size * 3 + 8, self.block_size),
            Block(self.block_size * 3, HEIGHT - self.block_size * 4 + 5, self.block_size),
            Block(666, HEIGHT - self.block_size * 4 + 10, self.block_size),
            Block(1200, HEIGHT - self.block_size * 4 + 10, self.block_size),
            Block(1200, HEIGHT - self.block_size * 5 + 12, self.block_size),
            Block(666, HEIGHT - self.block_size * 5 + 12, self.block_size),
            Block(0, HEIGHT - self.block_size * 6 + 5, self.block_size),
            Block(630, 255, self.block_size),
            Block(1050, 235, self.block_size),
            Block(1305, 405, self.block_size),
            Block(1375, 405, self.block_size),
            Block(1555, 405, self.block_size),
            Block(1650, 405, self.block_size),
            Block(1746, 405, self.block_size),
            Block(1842, 405, self.block_size),
            Block(1296, HEIGHT - self.block_size * 2 + 5, self.block_size),
            Block(1296, HEIGHT - self.block_size * 3 + 8, self.block_size),
            Block(1392, HEIGHT - self.block_size * 2 + 5, self.block_size),
            Block(1738, 496, self.block_size),
            Block(1834, 496, self.block_size),
            Block(1834, 589, self.block_size),
        ]

    def create_fires(self):
        fires = [
            Fire(110, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(400, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(170, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(460, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(230, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(520, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(800, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(830, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(860, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(890, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(920, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(950, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(980, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(1010, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(1040, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(1070, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(1100, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(1130, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(770, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(1160, HEIGHT - self.block_size - 64 + 5, 16, 32),
            Fire(0, 445, 16, 32),
            Fire(1200, 550, 16, 32),
            Fire(1260, 550, 16, 32),
            Fire(1310, 341, 16, 32),
            Fire(1370, 341, 16, 32),
            Fire(1430, 341, 16, 32),
            Fire(1555, 341, 16, 32),
            Fire(1615, 341, 16, 32),
            Fire(1675, 341, 16, 32),
            Fire(1735, 341, 16, 32),
            Fire(1795, 341, 16, 32),
            Fire(1855, 341, 16, 32)
        ]

        for fire in fires:
            fire.on()
        return fires

    def create_level(self):
        return self.create_floor() + self.create_blocks() + self.create_fires() 