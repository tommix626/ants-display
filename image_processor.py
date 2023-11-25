class ImageProcessor:
    @staticmethod
    def convert_time_to_dots(time_str, width, height):
        # Define the basic pattern for each digit in a 5x3 grid (rows x columns)
        def scale_pattern(pattern, scale):
            return [((x) * scale, y * scale) for (x, y) in pattern]

        # Patterns for the digits and colon
        basic_patterns = {
            '0': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
            '1': [(0, 1), (1, 0), (1, 1), (2, 1), (3, 1), (4, 0), (4, 1), (4, 2)],
            '2': [(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0), (4, 1), (4, 2)],
            '3': [(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
            '4': [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2)],
            '5': [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
            '6': [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
            '7': [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
            '8': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1),
                  (4, 2)],
            '9': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
            ':': [(1, 1), (3, 1)]  # Colon pattern
        }
        # Calculate scale and spacing based on width and height
        digit_height = 4  # Height of each digit pattern
        digit_width = 3  # Width of each digit pattern
        total_digits = 4  # 4 digits + 1 colon

        # Allow for some blank space on edges
        horizontal_margin = width // 10
        vertical_margin = height // 10

        available_width = width - 2 * horizontal_margin
        available_height = height - 2 * vertical_margin
        print(available_height)
        print(available_width)
        # Determine the scale for the patterns
        scale_x = int(available_height / digit_height)
        scale_y = int(available_width / (total_digits * digit_width))

        scale = min(scale_x, scale_y)
        print(scale_x,scale_y)
        # Function to position digit patterns
        def position_pattern(pattern, offset_x, offset_y):
            return [(x + offset_x, y + offset_y) for x, y in pattern]

        # Remove any non-digit characters except for colon from the time string
        time_str = ''.join(filter(lambda c: c.isdigit() or c == ':', time_str))

        # Calculate the offset for each digit based on its position in the time string
        dot_list = []
        offset_x = vertical_margin
        offset_y = horizontal_margin
        for digit in time_str:
            pattern = scale_pattern(basic_patterns[digit], scale)
            dot_list.extend(position_pattern(pattern, offset_x, offset_y))
            offset_y += digit_width * scale
            offset_y = int(offset_y)

        return dot_list

    @staticmethod
    def get_current_time():
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return current_time
