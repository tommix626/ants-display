import random
from datetime import datetime
import time
from ant import Ant
from canvas import Canvas
# from image_processor import ImageProcessor  # Uncomment and implement as needed

def get_dots_for_830():
    # Representation of digits in a 5x3 grid (rows x columns)
    digit_8 = [(x, y) for x in range(5) for y in range(3)]
    digit_3 = [(0, y) for y in range(3)] + [(2, y) for y in range(3)] + [(4, y) for y in range(3)] + [(1, 2), (3, 2)]
    digit_0 = [(0, y) for y in range(1, 3)] + [(4, y) for y in range(1, 3)] + [(x, 0) for x in range(5)] + [(x, 2) for x in range(5)]

    # Adjust the positions of each digit
    digit_8 = [(x, y) for x, y in digit_8]
    digit_3 = [(x, y + 4) for x, y in digit_3]  # Shift right by 4 units
    digit_0 = [(x, y + 8) for x, y in digit_0]  # Shift right by 8 units
    digit_3_2 = [(x, y + 12) for x, y in digit_3]  # Second '3', shift right by 12 units

    # Combine all digits to form "8:30"
    dot_list = digit_8 + digit_3 + digit_0 + digit_3_2
    return dot_list


def main():
    width, height = 100, 100  # Set the size of your canvas
    num_ants = 50  # Number of ants
    canvas = Canvas(width, height)
    ants = [Ant(random.randint(0, width - 1), random.randint(0, height - 1), canvas) for _ in range(num_ants)]

    # Testing dot list for "8:30"
    dot_list = get_dots_for_830()
    for x, y in dot_list:
        canvas.place_food_source(x, y)

    while True:
        # Move each ant and update the canvas
        for ant in ants:
            ant.move()

        canvas.evaporate_pheromones(evaporation_rate=0.1)  # Adjust evaporation rate as needed

        canvas.draw_canvas()  # Implement the visualization logic

        time.sleep(1)  # Update interval; adjust as needed for smoothness vs performance

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
