import pygame
import random
import time
import threading
from sorting_algorithms.bubblesort import sort as bubblesort
from sorting_algorithms.selectionsort import sort as selectionsort
from sorting_algorithms.insertionsort import sort as insertionsort
from sorting_algorithms.mergesort import sort as mergesort
from sorting_algorithms.quicksort import sort as quicksort
from sorting_algorithms.heapsort import sort as heapsort
from sorting_algorithms.radixsort import sort as radixsort
from sorting_algorithms.bucketsort import sort as bucketsort
from sorting_algorithms.timsort import sort as timsort
from sorting_algorithms.bogosort import sort as bogosort
import os

pygame.init()
pygame.font.init()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_PATH = os.path.join(BASE_DIR, 'assets', 'fonts')

font_title = pygame.font.Font(os.path.join(FONT_PATH, "Montserrat-Bold.ttf"), 60)
font_button = pygame.font.Font(os.path.join(FONT_PATH, "Montserrat-SemiBold.ttf"), 32)
font_input = pygame.font.Font(os.path.join(FONT_PATH, "Montserrat-Regular.ttf"), 28)
font_small = pygame.font.Font(os.path.join(FONT_PATH, "Montserrat-Light.ttf"), 24)

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
FPS = 60

WHITE = (255, 255, 255)
LIGHT_GRAY = (230, 230, 230)
SOFT_BLUE = (130, 180, 255)
DARK_GRAY = (50, 50, 50)
SOFT_GREEN = (100, 215, 100)
SOFT_AMBER = (255, 204, 102)
SOFT_RED = (255, 110, 100)
LIGHT_BLUE = (140, 210, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AlgoVista Sorting Visualizer")

def draw_button(text, x, y, width, height, color, font, radius=20):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect, border_radius=radius)
    txt_surf = font.render(text, True, WHITE)
    txt_rect = txt_surf.get_rect(center=rect.center)
    screen.blit(txt_surf, txt_rect)
    return rect

def show_text(text, x, y, color, font):
    screen.blit(font.render(text, True, color), (x, y))

def run_sorting_algorithm(selected_algo, search_space_size, result_message):
    algo_map = {
        "bubblesort": bubblesort,
        "selectionsort": selectionsort,
        "insertionsort": insertionsort,
        "mergesort": mergesort,
        "quicksort": quicksort,
        "heapsort": heapsort,
        "radixsort": radixsort,
        "bucketsort": bucketsort,
        "timsort": timsort,
        "bogosort": bogosort
    }
    data = [random.randint(1, 100) for _ in range(search_space_size)]
    sorted_arr = sorted(data)
    start = time.time()
    result = algo_map[selected_algo](data, sorted_arr)
    elapsed = time.time() - start
    result_message[0] = f"Sorting completed in {elapsed:.6f} seconds" if result else "Sorting took more than 20 seconds. [Failed]"

def show_loading_screen(timer, spinner_frame):
    screen.fill(SOFT_BLUE)
    loading_text = "Loading..."
    text_width = font_title.size(loading_text)[0]
    show_text(loading_text, (SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2 - 80, DARK_GRAY, font_title)

    spinner = " "
    spinner_char = spinner[spinner_frame % len(spinner)]
    show_text(f"{spinner_char}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, DARK_GRAY, font_title)

    show_text(f"Time: {int(timer)}s", SCREEN_WIDTH - 200, 20, DARK_GRAY, font_small)
    pygame.display.update()



def format_number_with_commas(number_str):
    return "{:,}".format(int(number_str))

def main():
    running = True
    menu_state = "main_menu"
    selected_algo_index = -1
    algorithm_list = ["bubblesort", "selectionsort", "insertionsort", "mergesort", "quicksort", "heapsort", "radixsort", "bucketsort", "timsort", "bogosort"]
    dropdown_open = False
    search_space_size = ""
    input_box_active = False
    result_message = [""]
    sorting_thread = None
    sorting_in_progress = False
    start_time = 0
    elapsed_time = 0
    spinner_frame = 0

    while running:
        screen.fill(LIGHT_GRAY)

        if menu_state == "main_menu":
            show_text("Welcome to AlgoVista Sorting Visualizer!", (SCREEN_WIDTH - font_title.size("Welcome to AlgoVista Sorting Visualizer!")[0]) // 2, 50, DARK_GRAY, font_title)
            show_text("Choose an option", (SCREEN_WIDTH - font_small.size("Choose an option")[0]) // 2, 150, DARK_GRAY, font_small)

            sorting_button = draw_button("Sorting Algorithms", (SCREEN_WIDTH - 400) // 2, 250, 400, 50, SOFT_BLUE, font_button)
            pathfinding_button = draw_button("Pathfinding Algorithms", (SCREEN_WIDTH - 400) // 2, 350, 400, 50, SOFT_BLUE, font_button)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if sorting_button.collidepoint(event.pos):
                        menu_state = "sorting_menu"

        elif menu_state == "sorting_menu":
            show_text("Sorting Algorithms", (SCREEN_WIDTH - font_title.size("Sorting Algorithms")[0]) // 2, 50, DARK_GRAY, font_title)
            input_box = pygame.Rect((SCREEN_WIDTH - 300) // 2, 250, 300, 40)
            pygame.draw.rect(screen, SOFT_BLUE, input_box, border_radius=15)
            pygame.draw.rect(screen, SOFT_AMBER if input_box_active else DARK_GRAY, input_box, 2)

            formatted_search_space_size = format_number_with_commas(search_space_size) if search_space_size else "0"
            show_text(formatted_search_space_size, (SCREEN_WIDTH - font_input.size(formatted_search_space_size)[0]) // 2, 255, DARK_GRAY, font_input)

            algo_dropdown_rect = pygame.Rect((SCREEN_WIDTH - 300) // 2, 320, 300, 40)
            pygame.draw.rect(screen, SOFT_BLUE, algo_dropdown_rect, border_radius=15)
            show_text("Select Algorithm", (SCREEN_WIDTH - font_small.size("Select Algorithm")[0]) // 2, 330, DARK_GRAY, font_small)

            if selected_algo_index != -1:
                show_text(f"{algorithm_list[selected_algo_index]}", (SCREEN_WIDTH - font_input.size(algorithm_list[selected_algo_index])[0]) // 2, 370, DARK_GRAY, font_input)
            else:
                show_text("None", (SCREEN_WIDTH - font_input.size("None")[0]) // 2, 370, DARK_GRAY, font_input)

            if dropdown_open:
                for i, algo in enumerate(algorithm_list):
                    item_rect = pygame.Rect((SCREEN_WIDTH - 300) // 2, 370 + (i + 1) * 45, 300, 40)
                    pygame.draw.rect(screen, SOFT_AMBER, item_rect, border_radius=10)
                    pygame.draw.rect(screen, DARK_GRAY, item_rect, 2)
                    show_text(algo, (SCREEN_WIDTH - font_input.size(algo)[0]) // 2, 380 + (i + 1) * 45, DARK_GRAY, font_input)
                    if pygame.mouse.get_pressed()[0] and item_rect.collidepoint(pygame.mouse.get_pos()):
                        selected_algo_index = i
                        dropdown_open = False

            back_button = draw_button("Back", 50, SCREEN_HEIGHT - 100, 300, 50, SOFT_RED, font_button)
            sort_button = draw_button("Sort", SCREEN_WIDTH - 350, SCREEN_HEIGHT - 100, 300, 50, SOFT_GREEN, font_button)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        menu_state = "main_menu"
                        selected_algo_index = -1
                        search_space_size = ""
                        input_box_active = False
                        result_message[0] = ""
                        sorting_in_progress = False
                        sorting_thread = None
                        elapsed_time = 0
                    elif sort_button.collidepoint(event.pos):
                        if selected_algo_index != -1 and search_space_size.replace(",", "").isdigit() and not sorting_in_progress:
                            sorting_in_progress = True
                            start_time = time.time()
                            sorting_thread = threading.Thread(target=run_sorting_algorithm, args=(algorithm_list[selected_algo_index], int(search_space_size.replace(",", "")), result_message))
                            sorting_thread.start()
                            menu_state = "loading"

                    elif algo_dropdown_rect.collidepoint(event.pos):
                        dropdown_open = not dropdown_open
                    elif input_box.collidepoint(event.pos):
                        input_box_active = True
                    else:
                        input_box_active = False

                elif event.type == pygame.KEYDOWN and input_box_active:
                    if event.key == pygame.K_BACKSPACE:
                        search_space_size = search_space_size[:-1]
                    elif event.unicode.isdigit():
                        new_val = search_space_size + event.unicode
                        new_val_without_commas = new_val.replace(",", "")
                        search_space_size = str(min(int(new_val_without_commas), 10000000))

        elif menu_state == "loading":
            
            elapsed_time = time.time() - start_time
            show_loading_screen(elapsed_time, spinner_frame)
            spinner_frame = (spinner_frame + 1) % 4  # Loop through spinner frames
            if not sorting_thread.is_alive():
                menu_state = "sorting_result"

        elif menu_state == "sorting_result":
            screen.fill(SOFT_BLUE)
            show_text("Sorting Complete!", (SCREEN_WIDTH - font_title.size("Sorting Complete!")[0]) // 2, 100, DARK_GRAY, font_title)
            show_text(result_message[0], (SCREEN_WIDTH - font_input.size(result_message[0])[0]) // 2, 250, DARK_GRAY, font_input)

            back_button = draw_button("Back", (SCREEN_WIDTH - 300) // 2, SCREEN_HEIGHT - 150, 300, 50, SOFT_RED, font_button)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        menu_state = "sorting_menu"
                        selected_algo_index = -1
                        search_space_size = ""
                        input_box_active = False
                        result_message[0] = ""
                        sorting_in_progress = False
                        sorting_thread = None
                        elapsed_time = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
