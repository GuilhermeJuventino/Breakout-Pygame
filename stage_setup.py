import pygame
import constants as c
import json

from elements.block import Block


def stage_setup(groups, obstacles, level=1):
    # Cycle through all rows and columns in BLOCK_MAP
    block_group = pygame.sprite.Group()

    file = open(f"levels/level{level}.json", "r")

    info = file.read()
    file.close()

    layout = json.loads(info)

    block_map = layout["BLOCK_MAP"]

    block_width = c.WIDTH / len(block_map) - 35 - c.GAP_SIZE
    block_height = c.HEIGHT / len(block_map[0]) - c.GAP_SIZE

    for row_index, row in enumerate(block_map):
        for col_index, col in enumerate(row):

            if col != " ":
                # Find the x and y position of each individual block
                x = col_index * (block_width + c.GAP_SIZE) + c.GAP_SIZE // 2
                y = c.TOP_OFFSET + row_index * (block_height + c.GAP_SIZE) + c.GAP_SIZE // 2
                block = Block(col, (x, y), groups, obstacles, block_width, block_height)
                block_group.add(block)

    return block_group
