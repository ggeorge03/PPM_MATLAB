import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the system parameters
m1 = 1.0   # mass of the disc (kg)
m2 = 0.5   # mass of the attached square (kg)
R = 1.0    # radius of the disc (m)
r = 0.5    # distance of the square from the center of the disc (m)
g = 9.81   # acceleration due to gravity (m/s^2)

# Define the moment of inertia constants
I_effective = (m2**2 * r**2) / (m1 + m2) + (1/2) * m1 * R**2 + m2 * r**2

# Define the equation of motion (theta'' = f(theta))


def equation_of_motion(t, y):
    theta, theta_dot = y
    theta_double_dot = - (m2 * g * r * np.cos(theta - np.pi)) / \
        I_effective  # theta = 0 is directly above
    return [theta_dot, theta_double_dot]


# Set initial conditions (theta = 0 where the mass is directly above center)
# initial angle (theta = 0 represents the mass directly above the center)
theta0 = 0.0
theta_dot0 = 0.0  # initial angular velocity (rad/s)

# Time span for the simulation (seconds)
t_span = [0, 10]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the differential equation
sol = solve_ivp(equation_of_motion, t_span, [
                theta0, theta_dot0], t_eval=t_eval)

# Extract solution
theta = sol.y[0]
theta_dot = sol.y[1]
time = sol.t

# Convert theta to multiples of pi
theta_pi = theta / np.pi

# Plot the results
plt.figure(figsize=(12, 6))

# Plot theta (angle) vs time, converted to multiples of pi
plt.subplot(2, 1, 1)
plt.plot(time, theta_pi, label=r'$\theta$(t)', color='blue')
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta$ (in units of $\pi$)')
plt.yticks(np.arange(-1.0, 1.25, 0.25),  # Adjusting the tick marks for theta in units of pi
           [r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{4}$', '0',
            r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
plt.title('Angular Position vs Time (in terms of $\pi$ radians)')
plt.grid(True)

# Plot theta_dot (angular velocity) vs time
plt.subplot(2, 1, 2)
plt.plot(time, theta_dot, label=r'$\dot{\theta}$(t)', color='green')
plt.xlabel('Time (s)')
plt.ylabel(r'$\dot{\theta}$ (rad/s)')
plt.title('Angular Velocity vs Time')
plt.grid(True)

plt.tight_layout()
plt.show()
