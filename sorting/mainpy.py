import pygame
import random
import time
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

pygame.init()

# Constants for the screen (increased size)
SCREEN_WIDTH = 1000  # Wider window
SCREEN_HEIGHT = 800  # Taller window
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (135, 206, 250)
DARK_BLUE = (30, 30, 60)
GREEN = (34, 177, 76)
RED = (255, 99, 71)
YELLOW = (255, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AlgoVista Sorting Visualizer")

font = pygame.font.SysFont('Arial', 24)
small_font = pygame.font.SysFont('Arial', 18)

# Helper functions
def draw_button(text, x, y, width, height, color, font, action=None):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)  # Rounded corners
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect

def show_text(text, x, y, color, font):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def run_sorting_algorithm(selected_algo, search_space_size):
    sorting_dict = {
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

    # Generate the random list based on the search space size
    data = [random.randint(1, 100) for _ in range(search_space_size)]
    sorted_arr = sorted(data)

    # Timing the sorting algorithm
    start_time = time.time()
    result = sorting_dict[selected_algo](data, sorted_arr)
    end_time = time.time()

    if result:
        return f"Sorting completed in {end_time - start_time:.6f} seconds"
    else:
        return "Sorting took more than 20 seconds."

def show_loading_screen():
    """Displays a loading screen with a spinning indicator or a loading message."""
    screen.fill(DARK_BLUE)
    show_text("Loading...", SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, WHITE, font)

    # Show loading spinner
    spinner = "|/-\\"
    for i in range(10):
        show_text(spinner[i % 4], SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 + 20, WHITE, font)
        pygame.display.update()
        time.sleep(0.1)
        screen.fill(DARK_BLUE)
        show_text("Loading...", SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, WHITE, font)

def main():
    running = True
    menu_state = "main_menu"
    selected_algo = None
    search_space_size = ""
    message = ""
    dropdown_open = False
    algorithm_list = ["bubblesort", "selectionsort", "insertionsort", "mergesort", "quicksort", "heapsort", 
                      "radixsort", "bucketsort", "timsort", "bogosort"]
    selected_algo_index = -1

    input_box_active = False  # Track if input box is active
    cursor_position = 0  # Position of the cursor in the input box

    while running:
        screen.fill(DARK_BLUE)

        if menu_state == "main_menu":
            show_text("Welcome to AlgoVista Sorting Visualizer!", 150, 50, WHITE, font)
            show_text("Choose an option", 350, 150, WHITE, font)

            sorting_button = draw_button("Sorting Algorithms", 350, 250, 300, 50, LIGHT_BLUE, font)
            pathfinding_button = draw_button("Pathfinding Algorithms", 350, 350, 300, 50, LIGHT_BLUE, font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sorting_button.collidepoint(event.pos):
                        menu_state = "sorting_menu"
                    if pathfinding_button.collidepoint(event.pos):
                        pass  # Add pathfinding menu when ready

        elif menu_state == "sorting_menu":
            show_text("Sorting Algorithms", 350, 50, WHITE, font)
            show_text("Select an algorithm and input the number of elements", 100, 150, WHITE, small_font)

            # Number of elements input box positioned above the algorithm dropdown
            input_box = pygame.Rect(350, 250, 300, 40)
            pygame.draw.rect(screen, LIGHT_BLUE, input_box, border_radius=10)

            # Input the current number or cursor text
            show_text(search_space_size if search_space_size else "0", 430, 255, BLACK, font)

            # Highlight if the input box is active
            if input_box_active:
                pygame.draw.rect(screen, YELLOW, input_box, 2)  # Active input box
            else:
                pygame.draw.rect(screen, BLACK, input_box, 2)  # Default border

            # Sorting algorithm dropdown below the number input
            algo_dropdown_rect = pygame.Rect(350, 320, 300, 40)
            pygame.draw.rect(screen, LIGHT_BLUE, algo_dropdown_rect, border_radius=10)
            show_text("Select Algorithm", 420, 330, BLACK, small_font)

            if selected_algo_index != -1:
                show_text(f"{algorithm_list[selected_algo_index]}", 420, 370, BLACK, font)
            else:
                show_text("None", 420, 370, BLACK, font)

            # Back button at bottom right
            back_button = draw_button("Back", SCREEN_WIDTH - 350, SCREEN_HEIGHT - 100, 300, 50, RED, font)

            # Sort button left-aligned near the bottom
            sort_button = draw_button("Sort", 50, SCREEN_HEIGHT - 100, 300, 50, GREEN, font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        menu_state = "main_menu"
                    if sort_button.collidepoint(event.pos):
                        # Show loading screen before sorting
                        menu_state = "loading_screen"
                    if algo_dropdown_rect.collidepoint(event.pos):
                        dropdown_open = not dropdown_open  # Toggle dropdown

                    # Handle the input box click event
                    if input_box.collidepoint(event.pos):
                        input_box_active = True
                    else:
                        input_box_active = False  # Deselect the input box if clicked outside

                # Handle KEYDOWN events only if the input box is clicked
                if event.type == pygame.KEYDOWN and input_box_active:
                    if event.key == pygame.K_BACKSPACE:
                        search_space_size = search_space_size[:-1]  # Remove last character
                    elif event.key == pygame.K_RETURN:
                        pass  # You can implement an action when 'Enter' is pressed if needed
                    else:
                        # Add character to the string if it's a digit
                        if event.unicode.isdigit():
                            search_space_size += event.unicode

                    # Ensure the number is valid (from 1 to 10 million)
                    if not search_space_size.isdigit():
                        search_space_size = ""
                    elif int(search_space_size) > 10000000:
                        search_space_size = "10000000"

            # Display the algorithm dropdown options if the dropdown is open
            if dropdown_open:
                # Draw a semi-transparent block behind the dropdown to prevent clicks behind it
                pygame.draw.rect(screen, (0, 0, 0, 128), (350, 320, 300, 40 * len(algorithm_list)))

                for i, algo in enumerate(algorithm_list):
                    dropdown_rect = pygame.Rect(350, 370 + i * 40, 300, 40)
                    pygame.draw.rect(screen, LIGHT_BLUE, dropdown_rect, border_radius=10)
                    show_text(algo, 420, 380 + i * 40, BLACK, small_font)
                    if event.type == pygame.MOUSEBUTTONDOWN and dropdown_rect.collidepoint(event.pos):
                        selected_algo_index = i
                        dropdown_open = False  # Close dropdown after selection

        elif menu_state == "loading_screen":
            show_loading_screen()
            if search_space_size:
                message = run_sorting_algorithm(algorithm_list[selected_algo_index], int(search_space_size))
            menu_state = "result_screen"

        elif menu_state == "result_screen":
            screen.fill(DARK_BLUE)
            show_text(f"Sorting Result: {message}", 150, 150, WHITE, font)
            back_button = draw_button("Back to Main Menu", SCREEN_WIDTH - 350, SCREEN_HEIGHT - 100, 300, 50, LIGHT_BLUE, font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        menu_state = "main_menu"

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
