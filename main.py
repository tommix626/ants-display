import random
from datetime import datetime
import time
from ant import Ant
from canvas import Canvas
from image_processor import ImageProcessor

def get_dots_for_830(scale=4, spacing=2):
    # Adjust scale and spacing to fit the grid size and visual preferences

    # Define a basic pattern for the digits in a 5x3 grid (rows x columns)
    def scale_pattern(pattern):
        return [(x * scale, y * scale) for (x, y) in pattern]

    # Patterns for the digits
    digit_8_pattern = scale_pattern([
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2),
        (3, 0),         (3, 2),
        (4, 0), (4, 1), (4, 2)
    ])

    digit_3_pattern = scale_pattern([
        (0, 0), (0, 1), (0, 2),
                        (1, 2),
        (2, 0), (2, 1), (2, 2),
                        (3, 2),
        (0, 0), (0, 1), (0, 2),
    ])

    digit_0_pattern = scale_pattern([
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0),         (2, 2),
        (3, 0),         (3, 2),
        (4, 0), (4, 1), (4, 2)
    ])

    # Calculate the offsets for each digit based on its width, scale, and spacing
    offset_8 = 0
    offset_3 = (3 * scale) + (spacing * scale)
    offset_0 = (2 * offset_3) + (spacing * scale)

    # Offset the patterns to create the "8:30" layout
    digit_8 = [(x, y + offset_8) for (x, y) in digit_8_pattern]
    digit_3_first = [(x, y + offset_3) for (x, y) in digit_3_pattern]
    digit_0 = [(x, y + offset_0) for (x, y) in digit_0_pattern]
    digit_3_second = [(x, y + offset_0 + offset_3) for (x, y) in digit_3_pattern]

    # Combine all digits to form the "8:30" layout
    dot_list = digit_8 + digit_3_first + digit_0 + digit_3_second

    return dot_list


def main():
    """core param"""
    width, height = 40, 100  # Set the size of your canvas
    num_ants = 200  # Number of ants
    ant_memory_size = 50
    ph_deposit, ph_multiplier = 1, 50
    active_mode_duration = 500

    """main"""
    last_updated_time = None

    canvas = Canvas(width, height)
    ants = [Ant(random.randint(0, width - 1), random.randint(0, height - 1), canvas,
                memory_size=ant_memory_size, pheromone_deposit=ph_deposit, active_pheromone_multiplier=ph_multiplier,
                active_mode_duration=active_mode_duration) for _ in range(num_ants)]

    # Testing dot list for "8:30"
    dot_list = get_dots_for_830()
    for x, y in dot_list:
        canvas.place_food_source(x, y)

    cnt=0
    while True:
        cnt+=1
        # if needed to update critical points
        current_time = ImageProcessor.get_current_time()
        if current_time != last_updated_time:
            current_time_dots = ImageProcessor.convert_time_to_dots(current_time,height,width)
            canvas.clear_critical_points()  # Clear previous critical points
            for x, y in current_time_dots:
                canvas.place_food_source(x, y)
            last_updated_time = current_time

        # Move each ant and update the canvas
        for ant in ants:
            ant.move()

        canvas.evaporate_pheromones(evaporation_rate=0.1)  # Adjust evaporation rate as needed
        if(cnt%30==0):
            canvas.draw_canvas_all(ants)  # Implement the visualization logic
        # time.sleep(1)  # Update interval; adjust as needed for smoothness vs performance

if __name__ == "__main__":
    main()

"""
def main():
    width, height = 100, 100  # Set the size of your canvas
    num_ants = 50  # Number of ants
    canvas = Canvas(width, height)
    ants = [Ant(random.randint(0, width - 1), random.randint(0, height - 1), canvas) for _ in range(num_ants)]

    while True:
        # Example: Update the canvas with new food sources based on the current time
        # Replace this with your actual image processing logic when ready
        # current_time = datetime.now()
        # image = ImageProcessor.convert_to_critical_points(current_time)  # Implement this method
        # for point in image:
        #     canvas.place_food_source(*point)

        # Move each ant and update the canvas
        for ant in ants:
            ant.move()

        canvas.evaporate_pheromones(evaporation_rate=0.1)  # Adjust evaporation rate as needed

        canvas.draw_canvas()  # Implement the visualization logic

        time.sleep(1)  # Update interval; adjust as needed for smoothness vs performance

if __name__ == "__main__":
    main()

"""
