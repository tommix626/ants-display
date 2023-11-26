import matplotlib.pyplot as plt

# Define a function to handle the click event
def on_click(event):
    if event.button == 1:  # Check if left mouse button was clicked
        print(f'Clicked at x={event.xdata}, y={event.ydata}')

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Connect the event handler function to the 'button_press_event'
fig.canvas.mpl_connect('button_press_event', on_click)

# Display the plot (you can replace this with your own data)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()