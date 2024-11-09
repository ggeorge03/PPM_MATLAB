import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define constants
m1 = 1.0  # mass 1 in kg
m2 = 0.75  # mass 2 in kg
g = 9.81  # acceleration due to gravity in m/s^2
r = 3.39  # radius r in meters
R = 5.0   # radius R in meters
mu = 0.01  # friction coefficient

# Create an array for theta from -pi/2 to 3*pi/2
theta_model = np.linspace(-np.pi / 2, 9 * np.pi / 2, 1000)

# Calculate alpha for each value of theta
numerator = m2 * g * r * np.sin(theta_model)
denominator = (m2**2 * r**2 / (m1 + m2)) + (0.5 * m1 * R**2) + (m2 * r**2)
theta_model = (numerator / denominator)

# Adjust theta to ensure the lowest value is zero
theta_model = theta_model - np.min(theta_model)
theta_model = theta_model * np.pi / 2

# Assume a uniform time step
time_model = np.linspace(0, 10, 1000)  # 10 seconds duration

# Apply time-dependent scaling factors
time_stretch_factor = 1 + mu * time_model  # Stretch factor increases over time
amplitude_decay_factor = np.exp(-0.1 * time_model)  # Exponential decay for amplitude

# Stretch the time array
time_model_stretched = time_model * time_stretch_factor

# Calculate angular velocity omega by differentiating theta with respect to time
omega_model = np.gradient(theta_model, time_model_stretched)

# Calculate angular acceleration by differentiating omega with respect to time and including friction
alpha_model = np.gradient(omega_model, time_model_stretched) - mu * omega_model

# Apply amplitude decay to theta, omega, and alpha
theta_model *= amplitude_decay_factor
omega_model *= amplitude_decay_factor
alpha_model *= amplitude_decay_factor

# Plot theta against time
plt.figure(figsize=(10, 5))
plt.plot(time_model_stretched, theta_model, 'b-')
plt.ylim(-1, 1.2 * np.pi)  # Set y-axis range
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta$ (radians)')
plt.title(r'Angle $\theta$ over time $t$')
plt.grid(True)
plt.show()

# Plot omega against time
plt.figure(figsize=(10, 5))
plt.plot(time_model_stretched, omega_model, 'b-')
plt.xlabel('Time (s)')
plt.ylabel(r'$\omega$ (rad/s)')
plt.title(r'Angular Velocity $\omega$ over time $t$')
plt.grid(True)
plt.show()

# Plot alpha against time
plt.figure(figsize=(10, 5))
plt.plot(time_model_stretched, alpha_model, 'b-')
plt.xlabel('Time (s)')
plt.ylabel(r'$\alpha$ (rad/s²)')
plt.title(r'Angular Acceleration $\alpha$ over time $t$')
plt.grid(True)
plt.show()
