import pygame
from math import sin, cos, radians

pygame.init()

map_surface = pygame.image.load("MAP1.png")
ground_color = (208, 208, 208)
wall_color = (128, 128, 128)

tank_image = pygame.image.load("GreenTank.png")
bullet = pygame.image.load("Bullet.png")


class Tank:

    def __init__(self, pos_x, pos_y, start_angle=180, image=tank_image):
        self.tank = image
        self.tank = pygame.transform.rotate(self.tank, start_angle)
        self.original_image = image

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = (self.pos_x, self.pos_y)

        self.rect = self.tank.get_rect(center=self.position)
        self.angle_up_down = self.angle_left_right = 0

    def move_left_right(self, direction):
        color = map_surface.get_at((self.pos_x + 15, self.pos_y + 15))
        if color != wall_color:
            if direction == "LEFT":
                    self.angle_left_right += 15
            elif direction == "RIGHT":
                self.angle_left_right -= 15
        self.tank = self.tank = pygame.transform.rotate(self.original_image, self.angle_left_right)
        self.rect = self.tank.get_rect(center=self.rect.center)

    def move_up_down(self, direction):
        color = map_surface.get_at((self.pos_x + 15, self.pos_y + 15))
        if color != wall_color:
            angle_rad = radians(self.angle_left_right)
            dx = dy = 0

            if direction == "DOWN":
              dx = 20 * sin(angle_rad)
              dy = 20 * cos(angle_rad)
            elif direction == "UP":
                dx = -20 * sin(angle_rad)
                dy = -20 * cos(angle_rad)
            self.rect.move_ip(dx, dy)


tank1 = Tank(70, 100)



class Screen:

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    FILL_COLOR = (30, 30, 30)

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        pygame.display.set_caption("Tank Battle: Duel")
        pygame.display.set_icon(tank_image)

    def show_screen(self):
        self.screen.fill(self.FILL_COLOR)

        running = True
        while running:
            self.screen.blit(map_surface, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        tank1.move_left_right("LEFT")

                    if event.key == pygame.K_d:
                        tank1.move_left_right("RIGHT")

                    if event.key == pygame.K_w:
                        tank1.move_up_down("UP")

                    if event.key == pygame.K_s:
                        tank1.move_up_down("DOWN")

            self.screen.blit(tank1.tank, tank1.rect)

            pygame.display.update()


screen = Screen()
screen.show_screen()
