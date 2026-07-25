import pygame

pygame.init()

path_pattern = lambda name: f"D:/PythonProjects/MySqlConnector/pythonProject1/BETA_Games/twodGame/Images/{name}"


class Unit:
    def __init__(self, name, x, y, length):
        self.NAME = name
        self.X = x
        self.Y = y
        self.LENGTH = length


unit1_path = lambda: pygame.image.load(path_pattern("unit1.png")).convert_alpha()
unit1 = Unit(unit1_path, 100, 100, 38)

unit2_path = lambda: pygame.image.load(path_pattern("unit2.png")).convert_alpha()
unit2 = Unit(unit2_path, 100, 200, 38)


class Screen:
    WIDTH = 1000
    HEIGHT = 512

    def __init__(self, _caption, _path):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load(path_pattern(_path)).convert_alpha()
        pygame.display.set_caption(_caption)

    def __call__(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            keys = pygame.key.get_pressed()
            color = lambda x, y: self.image.get_at((x, y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if keys[pygame.K_s] and unit1.Y + unit1.LENGTH + 1 <= self.HEIGHT and color(unit1.X, unit1.Y+unit1.LENGTH) != (0, 0, 0, 255):
                unit1.Y += 1
            if keys[pygame.K_w] and unit1.Y - 1 >= 0 and color(unit1.X, unit1.Y-1) != (0, 0, 0, 255):
                unit1.Y -= 1
            if keys[pygame.K_a] and unit1.X - 1 >= 0 and color(unit1.X-1, unit1.Y) != (0, 0, 0, 255):
                unit1.X -= 1
            if keys[pygame.K_d] and unit1.X + unit1.LENGTH + 1 <= self.WIDTH and color(unit1.X+unit1.LENGTH, unit1.Y) != (0, 0, 0, 255):
                unit1.X += 1

            if keys[pygame.K_DOWN] and unit2.Y + unit2.LENGTH + 1 <= self.HEIGHT and color(unit2.X, unit2.Y+unit2.LENGTH) != (0, 0, 0, 255):
                unit2.Y += 1
            if keys[pygame.K_UP] and unit2.Y - 1 >= 0 and color(unit2.X, unit2.Y-1) != (0, 0, 0, 255):
                unit2.Y -= 1
            if keys[pygame.K_LEFT] and unit2.X - 1 >= 0 and color(unit2.X-1, unit2.Y) != (0, 0, 0, 255):
                unit2.X -= 1
            if keys[pygame.K_RIGHT] and unit2.X + unit2.LENGTH + 1 <= self.WIDTH and color(unit2.X+unit2.LENGTH, unit2.Y) != (0, 0, 0, 255):
                unit2.X += 1

            self.screen.blit(self.image, (0, 0))
            self.screen.blit(unit1.NAME(), (unit1.X, unit1.Y))
            self.screen.blit(unit2.NAME(), (unit2.X, unit2.Y))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


caption = "2D Game"
map_name = "MAP.png"

main_screen = Screen(caption, map_name)
main_screen()
