import pygame
import os
import random
from enum import Enum
from collections import namedtuple

pygame.init()


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20

class SnakeGame:
    
    def __init__(self,w=640,h=480):
        self.w = w
        self.h = h
        
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        
        # init game state
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0 
        self.food = None
        self._place_food()
        
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE) // BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE) // BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        
        # collect user input
        
        # move
        
        # check if game over
        
        # place new food or just move
        
        # update ui and clock
        
        # return game over and score
        game_over = False
        return game_over, self.score


if __name__ == '__main__':
    game = SnakeGame()
    
    # Game loop
    while True:
        game_over, score = game.play_step()
        
        
        if game_over == True:
            break
        
        print("Score: ", score)
        
        # Break if game over
        pygame.quit()