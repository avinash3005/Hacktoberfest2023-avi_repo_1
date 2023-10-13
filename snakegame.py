import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
SNAKE_SIZE = 20
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize the Snake
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = (SNAKE_SIZE, 0)

# Initialize the food
food = (random.randint(0, (WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE, random.randint(0, (HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE)

# Score
score = 0

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, SNAKE_SIZE):
                snake_direction = (0, -SNAKE_SIZE)
            if event.key == pygame.K_DOWN and snake_direction != (0, -SNAKE_SIZE):
                snake_direction = (0, SNAKE_SIZE)
            if event.key == pygame.K_LEFT and snake_direction != (SNAKE_SIZE, 0):
                snake_direction = (-SNAKE_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-SNAKE_SIZE, 0):
                snake_direction = (SNAKE_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Check for collisions with the food
    if snake[0] == food:
        score += 1
        food = (random.randint(0, (WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE, random.randint(0, (HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE)
    else:
        snake.pop()

    # Check for collisions with the wall or itself
    if (
        snake[0][0] < 0
        or snake[0][0] >= WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= HEIGHT
        or snake[0] in snake[1:]
    ):
        game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(screen, GREEN, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

# Game over message
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, GREEN)
game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.update()

# Wait for a few seconds before closing the game
pygame.time.delay(2000)

# Quit the game
pygame.quit()
