import pygame
import random

# Main variables
window_height = 700
window_width = 800
block_size = 30
play_width = 300
play_height = 600
grid_pos_x = (window_width - play_width) // 2   # first block position on x
grid_pos_y = window_height - play_height - 10    # first block position on y

# Main colors
white = (200, 200, 200)
black = (0, 0, 0)

# Shapes
s = [[[0, 1, 1, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[1, 0, 0, 0],
      [1, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]]]

z = [[[1, 1, 0, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [1, 1, 0, 0],
      [1, 0, 0, 0],
      [0, 0, 0, 0]]]

i = [[[1, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0]],

     [[1, 1, 1, 1],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]]]

o = [[[1, 1, 0, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]]]

j = [[[1, 0, 0, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[1, 1, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0],
      [0, 0, 0, 0]],

     [[1, 1, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [0, 1, 0, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0]]]

l = [[[0, 0, 1, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[1, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0]],

     [[1, 1, 1, 0],
      [1, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[1, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]]]

t = [[[0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[1, 0, 0, 0],
      [1, 1, 0, 0],
      [1, 0, 0, 0],
      [0, 0, 0, 0]],

     [[1, 1, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]],

     [[0, 1, 0, 0],
      [1, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]]]


shapes = [s, z, i, o, j, l, t]


# Grid
def draw_grid():
    for e in range(21):
        for k in range(11):
            block_info = pygame.Surface((block_size, block_size))
            block_info.fill(white)
            window.blit(block_info, (grid_pos_x + k * block_size, grid_pos_y + e * block_size))
            pygame.draw.line(window, black, (grid_pos_x, grid_pos_y + e * block_size),
                             (grid_pos_x + play_width, grid_pos_y + e * block_size))
            pygame.draw.line(window, black, (grid_pos_x + k * block_size, grid_pos_y),
                             (grid_pos_x + k * block_size, grid_pos_y + play_height))


# Shapes
def get_shape():
    shape = random.choice(shapes)
    return shape


def draw_shape(x, y, shape):
    coord_list_right = []
    coord_list_bottom = []
    for obj in shape:
        for index_obj, num_list in enumerate(obj):
            for index_num, num in enumerate(num_list):
                if num > 0:
                    block = pygame.draw.rect(window, black, (x + index_num * block_size,
                                                             y + index_obj * block_size, block_size, block_size))
                    coord_list_right.append(block.right)
                    coord_list_bottom.append(block.bottom)
        return coord_list_right, coord_list_bottom


# Display surface
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tetris')
window.fill(white)


# Main game loop
def game_loop():
    run = True
    one_shape = True
    move_x = grid_pos_x + play_width // 2 - block_size
    move_y = grid_pos_y
    velocity = block_size
    block_coord_right = [0]   # coordinates of the block, x right side
    block_coord_bottom = [0]  # coordinates of the block, y bottom
    clock = pygame.time.Clock()

    while run:
        max_coord_x = max(block_coord_right)  # for adjusting coordinates by the shape
        max_coord_y = max(block_coord_bottom)   # for adjusting coordinates by the shape

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop

        if one_shape:
            draw_grid()
            shape = get_shape()
            block_coord_right, block_coord_bottom = draw_shape(move_x, move_y, shape)
            one_shape = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            draw_grid()
            rotated_shape = [shape[-1]] + shape[0:-1]   # rotating list shape in order to rotate a figure,
            # by removing last element and appending it in front
            shape = rotated_shape   # saving rotated shape into an old list that I could rotate it multiple times
            block_coord_right, block_coord_bottom = draw_shape(move_x, move_y, shape)

        if keys[pygame.K_RIGHT] and max_coord_x < grid_pos_x + play_width:    # boundaries: right 550
            draw_grid()
            move_x += velocity
            block_coord_right, block_coord_bottom = draw_shape(move_x, move_y, shape)

        if keys[pygame.K_LEFT] and move_x > grid_pos_x:  # boundaries: left 250
            draw_grid()
            move_x -= velocity
            block_coord_right, block_coord_bottom = draw_shape(move_x, move_y, shape)

        if clock.tick(6) and max_coord_y < grid_pos_y + play_height:    # boundaries: bottom 690
            draw_grid()
            move_y += velocity
            block_coord_right, block_coord_bottom = draw_shape(move_x, move_y, shape)
            print(max_coord_y)

        pygame.display.update()

    pygame.quit()  # If we exit the loop this will execute and close our game


if __name__ == '__main__':
    game_loop()
