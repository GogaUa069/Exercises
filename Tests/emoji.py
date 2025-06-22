import pygame

# Initialize Pygame
pygame.init()

# Load a PNG image (replace 'path_to_image.png' with your actual file path)
image = pygame.image.load(r"C:\Users\Егор\OneDrive\Рабочий стол\ai gen\TicTacToe.png")

# Create a display window (optional, but needed for displaying the image)
screen = pygame.display.set_mode((image.get_width(), image.get_height()))
pygame.display.set_caption("Loaded PNG Image")

# Display the image on the screen
screen.blit(image, (0, 0))
pygame.display.flip()

# Wait for a while (you can add more logic here)
pygame.time.delay(5000)

# Clean up and quit
pygame.quit()