from utils import pygame, time


def spear_trap(grid, enemies, start_row, start_col, direction, screen, tile_mapping, GP_TILE_WIDTH, GP_TILE_HEIGHT, draw_grid_fn):
    spear_char = "»" if direction == "right" else "«"
    dc = 1 if direction == "right" else -1
    col = start_col + dc
    row = start_row
    prev_pos = None

    while 0 <= col < len(grid[0]):
        tile = grid[row][col]

        if tile in {"#", "X"}:
            break  # stop at wall

        # Kill enemy
        if tile in {"1", "2", "3"}:
            enemies[tile][:] = [e for e in enemies[tile] if not (e["row"] == row and e["col"] == col)]
            grid[row][col] = " "

        # Clear previous spear tile
        if prev_pos:
            pr, pc = prev_pos
            if grid[pr][pc] == spear_char:
                grid[pr][pc] = " "

        # Draw new spear tile
        prev_pos = (row, col)
        grid[row][col] = spear_char

        draw_grid_fn()
        pygame.display.flip()
        pygame.time.wait(40)

        col += dc

    # Clear final spear
    if prev_pos:
        pr, pc = prev_pos
        if grid[pr][pc] == spear_char:
            grid[pr][pc] = " "
    draw_grid_fn()
    pygame.display.flip()

def freeze_trap(freeze_duration_ms, get_ticks_fn, set_freeze_effect_fn):
    """
    Freezes all enemies by setting a freeze effect duration (in milliseconds).
    """
    current_time = get_ticks_fn()
    set_freeze_effect_fn(current_time + freeze_duration_ms)

def blindness_trap(duration_ms, get_ticks_fn, set_invisible_effect_fn):
    """
    Makes the player invisible for a set duration (in ms).
    """
    current_time = get_ticks_fn()
    set_invisible_effect_fn(current_time + duration_ms)
