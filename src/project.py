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
    def __init__(self, image_path):
        self.pos = [
            random.randint(100, 1820),
            random.randint(100, 980)
        ]
        self.speed = random.uniform(1, 2)
        self.angle = random.uniform(0, 2 * math.pi)
        self.image = pygame.image.load(image_path)
        self.image_scale = pygame.transform.scale(self.image,(50, 30))
    
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

class PlayerFish:
    ...

class Food:
    ...

def draw_aquarium():
    ...

def display_score():
    ...

def main():
    pygame.init
    resolution = (1920,1080)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Aquarium Simulation")

    clock = pygame.time.Clock()

    background = pygame.image.load("background.png")
    fish_image = pygame.image.load("fish.png")
    player_image = pygame.image.load("player_fish.png")
    food_image = pygame.image.load("food.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()