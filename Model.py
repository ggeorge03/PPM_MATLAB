import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd

filepath = "MaxRadiusTestData.csv"
test_data = pd.read_csv(filepath)

x_blue = np.array((test_data['Blue x Values']))
y_blue = np.array((test_data['Blue y Values']))
x_red = np.array((test_data['Red x Values']))
y_red = np.array((test_data['Red y Values']))
time_exp = np.array((test_data['time']))

radius_of_mass_2 = np.max(y_blue)

# Define the system parameters
m1 = 0.02   # mass of the disc (kg)
m2 = 0.001   # mass of the attached square (kg)
R = 5      # radius of the disc (m)
r = 3.39   # distance of the square from the center of the disc (m)
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
t_span = [0, 1]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the differential equation
sol = solve_ivp(equation_of_motion, t_span, [
                theta0, theta_dot0], t_eval=t_eval)

# Extract solution
theta_model = sol.y[0]
theta_dot_model = sol.y[1]
theta_double_dot_model = (m2 * g * r * np.cos(theta_model)) / I_effective
time_model = sol.t

# Experimental angular position calculation
theta_exp = np.arccos(
    (y_blue - y_red) / np.sqrt((x_blue - x_red)**2 + (y_blue - y_red)**2))

theta_exp = theta_exp[11:32]
time_sliced = time_exp[11:32] - np.min(time_exp[11:32])

omega_exp = np.gradient(theta_exp, time_sliced)

alpha_exp = np.gradient(omega_exp, time_sliced)

# Plot angular velocity and angular acceleration
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Angular velocity plot
ax[0].plot(time_model, theta_dot_model,
           label=r'$\dot{\theta}$ (Angular Velocity)', color='blue')
ax[0].plot(time_sliced, omega_exp, 'r--',
           label="Experimental angular velocity")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel(r'Angular Velocity $\dot{\theta}$ (rad/s)')
ax[0].set_title("Angular Velocity vs Time")
ax[0].grid(True)
ax[0].legend()

# Angular acceleration plot
ax[1].plot(time_model, theta_double_dot_model,
           label=r'$\ddot{\theta}$ (Angular Acceleration)', color='green')
ax[1].plot(time_sliced, alpha_exp, 'r--',
           label="Experimental angular acceleration")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel(r'Angular Acceleration $\ddot{\theta}$ (rad/s²)')
ax[1].set_title("Angular Acceleration vs Time")
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()

# Plot trajectory of the mass
# plt.figure(figsize=(10, 6))
# plt.plot(x_mass, y_mass, color='magenta', label="Equation of Motion")
# plt.plot(x_blue, y_blue, 'bo-', label='Experimental Trajectory')
# plt.xlabel("X position (cm)")
# plt.ylabel("Y position (cm)")
# plt.title(
#     "Comparison of Equation of Motion Trajectory and Experimental Data (r = 2.58cm)")
# plt.grid(True)
# plt.axis('equal')
# plt.legend()


# x_blue = np.array((test_data['Blue x Values']))
# y_blue = np.array((test_data['Blue y Values']))

# x_red = np.array((test_data['Red x Values']))
# y_red = np.array((test_data['Red y Values']))

# time = np.array((test_data['time']))

# radius_of_mass_2 = np.max(y_blue) - 5


# Convert from x and y coords to theta from vertical
# theta = np.arccos((y_blue-y_red)/np.sqrt((x_blue-x_red)**2+(y_blue-y_red)**2))

# Slice theta arrays from index 13 to 33 to remove static points of experiment
# theta = theta[11:32]
# time_sliced = time[11:32]
# time_sliced = time_sliced-np.min(time_sliced)


# Calculate angular velocity omega
# omega = np.gradient(theta, time_sliced)

# # Plot angular velocity omega against time_sliced
# plt.figure(figsize=(10, 5))
# plt.plot(time_sliced, omega, 'r-')
# plt.xlabel('Time (s)')
# plt.ylabel(r'$\omega$ (rad/s)')
# plt.title(
#     f'Angular Velocity $\omega$ over Time with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
# plt.grid(True)
# plt.show()


# # Plot theta against time
# plt.figure(figsize=(10, 5))
# plt.plot(time_sliced, theta, 'b-')
# plt.ylim(-1*np.pi, 2*np.pi)  # Set y-axis range
# plt.xlabel('Time (s)')
# plt.ylabel(r'$\theta$ (radians)')
# plt.title(
#     f'Angle $\\theta$ from the Vertical over Time with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
# plt.grid(True)
# # plt.show()


# Calculate angular acceleration alpha


# Plot angular acceleration alpha against time_sliced
# plt.figure(figsize=(10, 5))
# plt.plot(time_sliced, alpha, 'g-')
# plt.xlabel('Time (s)')
# plt.ylabel(r'$\alpha$ (rad/s²)')
# plt.title(
#     f'Angular Acceleration $\\alpha$ over Time with\nRadius of second mass: {radius_of_mass_2:.2f} cm')
# plt.grid(True)
# plt.show()
