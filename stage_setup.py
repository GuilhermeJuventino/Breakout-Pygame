import pygame
import constants as c

from elements.block import Block


def stage_setup(groups, obstacles):
    # Cycle through all rows and columns in BLOCK_MAP
    block_group = pygame.sprite.Group()

    for row_index, row in enumerate(c.BLOCK_MAP):
        for col_index, col in enumerate(row):

            if col != " ":
                # Find the x and y position of each individual block
                x = col_index * (c.BLOCK_WIDTH + c.GAP_SIZE) + c.GAP_SIZE // 2
                y = c.TOP_OFFSET + row_index * (c.BLOCK_HEIGHT + c.GAP_SIZE) + c.GAP_SIZE // 2
                block = Block(col, (x, y), groups, obstacles)
                block_group.add(block)

    return block_group
