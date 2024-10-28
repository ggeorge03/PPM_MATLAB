import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "Test Data/MediumRadiusTestData.csv"  # set path to the csv file
test_data = pd.read_csv(filepath)

x_blue = np.array((test_data['Blue x Values']))
y_blue = np.array((test_data['Blue y Values']))

x_red = np.array((test_data['Red x Values']))
y_red = np.array((test_data['Red y Values']))

time = np.array((test_data['time']))

radius_of_mass_2 = np.max(y_blue) - 5

# Plot positions
plt.figure(figsize=(10, 5))
plt.plot(x_blue, y_blue, 'bo-', label='Blue Dot Position')
plt.plot(x_red, y_red, 'ro-', label='Red Dot Position')
plt.xlabel('X Position (cm)')
plt.ylabel('Y Position (cm)')
plt.title(
    f'Positions of Blue and Red Dots with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# Calculate velocities
vx_blue = np.gradient(x_blue, time)
vy_blue = np.gradient(y_blue, time)
vx_red = np.gradient(x_red, time)
vy_red = np.gradient(y_red, time)

# Plot velocities using quiver plot
plt.figure(figsize=(10, 5))
plt.quiver(x_blue, y_blue, vx_blue, vy_blue, color='b',
           label='Blue Dot Velocity', width=0.0035)
plt.quiver(x_red, y_red, vx_red, vy_red, color='r',
           label='Red Dot Velocity', width=0.0035)
plt.xlabel('X Position (cm)')
plt.ylabel('Y Position (cm)')
plt.title(
    f'Velocities of Blue and Red Dots with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# Calculate accelerations
ax_blue = np.gradient(vx_blue, time)
ay_blue = np.gradient(vy_blue, time)
ax_red = np.gradient(vx_red, time)
ay_red = np.gradient(vy_red, time)

# Plot accelerations using quiver plot
plt.figure(figsize=(10, 5))
plt.quiver(x_blue, y_blue, ax_blue, ay_blue, color='b',
           label='Blue Dot Acceleration', width=0.0035)
plt.quiver(x_red, y_red, ax_red, ay_red, color='r',
           label='Red Dot Acceleration', width=0.0035)
plt.xlabel('X Position (cm)')
plt.ylabel('Y Position (cm)')
plt.title(
    f'Accelerations of Blue and Red Dots with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# Calculate magnitudes of velocities
v_blue = np.sqrt(vx_blue**2 + vy_blue**2)
v_red = np.sqrt(vx_red**2 + vy_red**2)

# Plot magnitudes of velocities over x-axis
plt.figure(figsize=(10, 5))
plt.plot(x_blue, v_blue, 'b-', label='Blue Dot Velocity Magnitude')
plt.plot(x_red, v_red, 'r-', label='Red Dot Velocity Magnitude')
plt.xlabel('X Position (cm)')
plt.ylabel('Velocity Magnitude (cm/s)')
plt.title(
    f'Velocity Magnitude over X Position with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.legend()
plt.grid(True)
plt.show()

# Calculate magnitudes of accelerations
a_blue = np.sqrt(ax_blue**2 + ay_blue**2)
a_red = np.sqrt(ax_red**2 + ay_red**2)

# Plot magnitudes of accelerations over x-axis
plt.figure(figsize=(10, 5))
plt.plot(x_blue, a_blue, 'b-', label='Blue Dot Acceleration Magnitude')
plt.plot(x_red, a_red, 'r-', label='Red Dot Acceleration Magnitude')
plt.xlabel('X Position (cm)')
plt.ylabel('Acceleration Magnitude (cm/s²)')
plt.title(
    f'Acceleration Magnitude over X Position with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.legend()
plt.grid(True)
plt.show()

# Convert from x and y coords to theta from vertical
theta = np.arccos((y_blue-y_red)/np.sqrt((x_blue-x_red)**2+(y_blue-y_red)**2))

# Slice theta arrays from index 13 to 33 to remove static points of experiment
theta = theta[11:32]
time_sliced = time[11:32]
time_sliced = time_sliced-np.min(time_sliced)

# Plot theta against time
plt.figure(figsize=(10, 5))
plt.plot(time_sliced, theta, 'b-')
plt.ylim(-1*np.pi, 2*np.pi)  # Set y-axis range
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta$ (radians)')
plt.title(
    f'Angle $\\theta$ from the Vertical over Time with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.grid(True)
plt.show()

# Calculate angular velocity omega
omega = np.gradient(theta, time_sliced)

# Plot angular velocity omega against time_sliced
plt.figure(figsize=(10, 5))
plt.plot(time_sliced, omega, 'r-')
plt.xlabel('Time (s)')
plt.ylabel(r'$\omega$ (rad/s)')
plt.title(
    f'Angular Velocity $\omega$ over Time with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.grid(True)
plt.show()

# Calculate angular acceleration alpha
alpha = np.gradient(omega, time_sliced)

# Plot angular acceleration alpha against time_sliced
plt.figure(figsize=(10, 5))
plt.plot(time_sliced, alpha, 'g-')
plt.xlabel('Time (s)')
plt.ylabel(r'$\alpha$ (rad/s²)')
plt.title(
    f'Angular Acceleration $\\alpha$ over Time with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
plt.grid(True)
plt.show()
