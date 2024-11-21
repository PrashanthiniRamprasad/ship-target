# Write your code here :-)
import random
import itertools
import pgzrun


WIDTH = 400
HEIGHT = 400


# Define four sets of coordinates for the block to move between
BLOCK_POSITIONS = [
    (350, 50),
    (350, 350),
    (50, 350),
    (50, 50),
]
# The "cycle()" function will let us cycle through the positions indefinitely
block_positions = itertools.cycle(BLOCK_POSITIONS)


block = Actor('block', center=(50, 50))
ship = Actor('ship', center=(200, 200))
