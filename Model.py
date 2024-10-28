import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd

# Load the experimental data
filepath = "MediumRadiusTestData.csv"  # set path to the csv file
test_data = pd.read_csv(filepath)

x_blue = np.array((test_data['Blue x Values'])) - 5
y_blue = np.array((test_data['Blue y Values'])) - 5
x_red = np.array((test_data['Red x Values']))
y_red = np.array((test_data['Red y Values']))
time_exp = np.array((test_data['time']))

radius_of_mass_2 = np.max(y_blue) - 5

# Define the system parameters
m1 = 1.0   # mass of the disc (kg)
m2 = 0.5   # mass of the attached square (kg)
R = 5      # radius of the disc (m)
r = 2.58   # distance of the square from the center of the disc (m)
g = 9.81   # acceleration due to gravity (m/s^2)

# Define the moment of inertia constants
I_effective = (m2**2 * r**2) / (m1 + m2) + (1/2) * m1 * R**2 + m2 * r**2

# Define the equation of motion (theta'' = f(theta))


def equation_of_motion(t, y):
    theta, theta_dot = y
    theta_double_dot = (m2 * g * r * np.cos(theta)) / I_effective
    return [theta_dot, theta_double_dot]


# Set initial conditions
theta0 = 0.0
theta_dot0 = 0.0

# Time span for the simulation
t_span = [0, 10]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the differential equation
sol = solve_ivp(equation_of_motion, t_span, [
                theta0, theta_dot0], t_eval=t_eval)

# Extract solution
theta = sol.y[0]
theta_dot = sol.y[1]
time = sol.t

# Compute x and y positions for the disc and mass as it rolls
x_center = R * theta
x_mass = x_center + r * np.sin(theta)
y_mass = r * np.cos(theta)

# Calculate angular acceleration
theta_double_dot = (m2 * g * r * np.cos(theta)) / I_effective

# Plot trajectory of the mass
plt.figure(figsize=(10, 6))
plt.plot(x_mass, y_mass, color='magenta', label="Equation of Motion")
plt.plot(x_blue, y_blue, 'bo-', label='Experimental Trajectory')
plt.xlabel("X position (cm)")
plt.ylabel("Y position (cm)")
plt.title(
    "Comparison of Equation of Motion Trajectory and Experimental Data (r = 2.58cm)")
plt.grid(True)
plt.axis('equal')
plt.legend()

# Plot angular velocity and angular acceleration
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Angular velocity plot
ax[0].plot(time, theta_dot,
           label=r'$\dot{\theta}$ (Angular Velocity)', color='blue')
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel(r'Angular Velocity $\dot{\theta}$ (rad/s)')
ax[0].set_title("Angular Velocity vs Time")
ax[0].grid(True)
ax[0].legend()

# Angular acceleration plot
ax[1].plot(time, theta_double_dot,
           label=r'$\ddot{\theta}$ (Angular Acceleration)', color='green')
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel(r'Angular Acceleration $\ddot{\theta}$ (rad/s²)')
ax[1].set_title("Angular Acceleration vs Time")
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
