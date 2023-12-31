import random
from datetime import datetime
import time
from ant import Ant
from canvas import Canvas
from image_processor import ImageProcessor


def main():
    """core param"""
    area_scale = 4
    width, height = 20 * area_scale, 100 * area_scale  # Set the size of your canvas
    num_ants = 10 * area_scale * 4 # Number of ants
    ant_memory_size = 17 * area_scale
    ph_deposit, ph_multiplier = 0.001, 600
    active_mode_duration = 6.5 * area_scale
    lin_evap_rate, exp_evap_rate = 0.1, 0.8

    """main"""
    last_updated_time = None

    canvas = Canvas(width, height)
    ants = [Ant(random.randint(0, width - 1), random.randint(0, height - 1), canvas,
                memory_size=ant_memory_size, pheromone_deposit=ph_deposit, active_pheromone_multiplier=ph_multiplier,
                active_mode_duration=active_mode_duration) for _ in range(num_ants)]

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

        canvas.evaporate_pheromones(lin_evap_rate, exp_evap_rate)  # Adjust evaporation rate as needed
        if( cnt% 3 ==0):
            canvas.draw_canvas_update(ants)  # Implement the visualization logic
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
