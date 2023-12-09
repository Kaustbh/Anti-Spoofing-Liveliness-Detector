     

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation

# Define the tire radius and initial position
tire_radius = 2
initial_position = np.array([2, 2], dtype=float)

# Define the final position
final_position = np.array([100, 2], dtype=float)

# Create a list to store the coordinates of the tire during its movement
coordinates = []

# Create a function to plot the tire at a given position with center coordinates
def plot_tire(position, angle):
    # Create the tire as a circle
    tire_circle = plt.Circle((position[0], position[1]), tire_radius, fill=False)
    plt.gca().add_patch(tire_circle)

    # Calculate the coordinates for the spokes
    spoke_length = tire_radius
    for i in range(4):
        x1 = position[0] - spoke_length * np.cos(angle)
        x2 = position[0] + spoke_length * np.cos(angle)
        y1 = position[1] - spoke_length * np.sin(angle)
        y2 = position[1] + spoke_length * np.sin(angle)

        # Draw the spokes
        spoke = Polygon([[x1, y1], [x2, y2]], fill=False, edgecolor='red')
        plt.gca().add_patch(spoke)
        angle += np.pi / 2

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 105)
ax.set_ylim(-5, 5)
ax.set_aspect('equal', adjustable='box')

# Animation update function
def update(frame):
    ax.clear()
    plt.xlim(-5, 105)
    plt.ylim(-5, 5)
    current_position = initial_position + frame * step_size
    plot_tire(current_position, frame * (-np.pi / 18))
    plt.gca().set_aspect('equal', adjustable='box')

# Number of frames for the animation
num_frames = 100

# Calculate step size
step_size = (final_position - initial_position) / num_frames

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, repeat=False)

# Display the animation
plt.show()