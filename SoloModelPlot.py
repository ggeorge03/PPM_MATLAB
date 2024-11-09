import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define constants
m1 = 1.0  # mass 1 in kg
m2 = 0.75  # mass 2 in kg
g = 9.81  # acceleration due to gravity in m/s^2
r = 3.39  # radius r in meters
R = 5.0   # radius R in meters
mu = 1.0  # friction coefficient

# Create an array for theta from -pi/2 to 9*pi/2
theta = np.linspace(-np.pi / 2, 9 * np.pi / 2, 1000)

# Define the denominator for the angular acceleration equation
denominator = (m2**2 * r**2 / (m1 + m2)) + (0.5 * m1 * R**2) + (m2 * r**2)

# Define the differential equation for omega
def d_omega_dt(omega, t, theta, m2, g, r, mu, denominator):
    theta_t = np.interp(t, time, theta)  # Interpolate theta at time t
    numerator = m2 * g * r * np.sin(theta_t) - mu * omega
    alpha = numerator / denominator
    return alpha

# Assume a uniform time step
time = np.linspace(0, 10, 1000)  # 10 seconds duration

# Initial angular velocity
omega0 = 0.0

# Solve the differential equation for omega
omega = odeint(d_omega_dt, omega0, time, args=(theta, m2, g, r, mu, denominator)).flatten()

# Calculate angular acceleration by differentiating omega with respect to time
alpha = np.gradient(omega, time)

# Plot omega against time
plt.figure(figsize=(10, 5))
plt.plot(time, omega, 'b-')
plt.xlabel('Time (s)')
plt.ylabel(r'$\omega$ (rad/s)')
plt.title(r'Angular Velocity $\omega$ over time $t$')
plt.grid(True)
plt.show()

# Plot alpha against time
plt.figure(figsize=(10, 5))
plt.plot(time, alpha, 'b-')
plt.xlabel('Time (s)')
plt.ylabel(r'$\alpha$ (rad/s²)')
plt.title(r'Angular Acceleration $\alpha$ over time $t$')
plt.grid(True)
plt.show()