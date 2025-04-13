# Lab15_apisani -1 
# Alex Pisani
# Aug 8 2024
# plots the circumfrence of a circle

import numpy as np
import matplotlib.pyplot as plt

# Number of points
num_points = 360

# Generate angles in degrees
angles_degrees = np.linspace(0, 360, num_points)

# Convert angles to radians
angles_radians = np.radians(angles_degrees)

# Calculate x and y coordinates
x = np.cos(angles_radians)
y = np.sin(angles_radians)

# Plotting the circle
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Circumference of the Circle')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circumference of a Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()