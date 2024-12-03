# Import pygame, random, and math libraries
# Set the game resolution
# Create main function for game
# Import images for game assets
# Create a class for fish AI
# Create movement for fish AI
# Use image asset for fish AI
# Create a class for fish player
# Create player controller for fish player
# Use image asset for fish player
# Check if player collects food
# Create a class for fish food
# Create a function for score display of food collected
# Create a function to create the aquarium background

import pygame
import random
import math

class Fish:
    def __init__(self, image):
        self.pos = [
            random.randint(100, 1820),
            random.randint(100, 980)
        ]
        self.speed = random.uniform(1, 2)
        self.angle = random.uniform(0, 2 * math.pi)

        self.size = random.uniform(0.1, 0.2)

        original_width, original_height = image.get_size()
        scaled_width = int(original_width * self.size)
        scaled_height = int(original_height * self.size)
        self.image_scaled = pygame.transform.scale(image, (scaled_width, scaled_height))
    
    def move(self):
        self.pos[0] += self.speed * math.cos(self.angle)
        self.pos[1] += self.speed * math.sin(self.angle)

        if self.pos[0] < 0:
            self.pos[0] = 1920
        elif self.pos[0] > 1920:
            self.pos[0] = 0

        if self.pos[1] < 0:
            self.pos[1] = 1080
        elif self.pos[1] > 1080:
            self.pos[1] = 0

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image_scaled, -math.degrees(self.angle))
        rect = rotated_image.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        screen.blit(rotated_image, rect.topleft)

class PlayerFish:
    def __init__(self, image, start_pos=(960, 540)):
        self.pos = list(start_pos)
        self.speed = 5
        self.image = image
        self.image_scaled = pygame.transform.scale(self.image, (150, 90))
        self.angle = 0

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.speed
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
            self.angle = 180
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
            self.angle = 0

        self.pos[0] = max(0, min(1920, self.pos[0]))
        self.pos[1] = max(0, min(1080, self.pos[1]))

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image_scaled, self.angle)
        rect = rotated_image.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        screen.blit(rotated_image, rect.topleft)

class Food:
    def __init__(self, image):
        self.pos = [
            random.randint(50, 1870),
            random.randint(50, 1030)
        ]
        self.image = pygame.transform.scale(image, (30, 30))

    def draw(self, screen):
        screen.blit(self.image, self.pos)

def check_collision(player, food):
    player_rect = pygame.Rect(player.pos[0] - 75, player.pos[1] - 45, 150, 90)
    food_rect = pygame.Rect(food.pos[0], food.pos[1], 30, 30)
    return player_rect.colliderect(food_rect)

# def draw_aquarium():
    ...

# def display_score():
    ...

def main():
    pygame.init()
    resolution = (1920,1080)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Aquarium Simulation")

    clock = pygame.time.Clock()

    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, resolution)

    fish_image = pygame.image.load("fish.png")
    player_image = pygame.image.load("player_fish.png")

    food_image = pygame.image.load("food.png")

    fish_list = [Fish(fish_image) for _ in range(10)]

    player_fish = PlayerFish(player_image)

    food_list = [Food(food_image) for _ in range(5)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player_fish.move(keys)

        screen.blit(background, (0, 0))

        for fish in fish_list:
            fish.move()
            fish.draw(screen)

        for food in food_list[:]:
            if check_collision(player_fish, food):
                food_list.remove(food)
            else:
                food.draw(screen)

        player_fish.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()