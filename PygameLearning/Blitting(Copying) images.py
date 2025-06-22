import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Copying images!")

skeleton_image = pygame.image.load(r"C:\Users\Егор\Downloads\skeleton-24735.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.blit(skeleton_image, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
    pygame.display.update()

pygame.quit()
