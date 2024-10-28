# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:02:07 2024

@author: cvhoh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
m1 = 1.0  # Mass 1 (kg)
m2 = 1.0  # Mass 2 (kg)
g = 9.81  # Acceleration due to gravity (m/s^2)
r = 1.0   # Length scale (m)
R = 1.0   # Length scale (m)
omega = 1.0  # Some constant (rad/s)

# ODE function
def odefun(t, y):
    theta, theta_dot = y
    dtheta_dt = theta_dot
    dtheta_dot_dt = -((m2 * g * r * np.sin(theta)) / (m1 * R**2 + m2 * r**2))
    return [dtheta_dt, dtheta_dot_dt]

# Initial conditions: [theta(0), theta_dot(0)]
theta0 = np.pi / 4  # Initial angle (radians)
theta_dot0 = 0.0    # Initial angular velocity (rad/s)
init_conditions = [theta0, theta_dot0]

# Time span
t_span = (0, 10)  # Solve from t = 0 to t = 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 100)  # Time points to evaluate

# Solve ODE
solution = solve_ivp(odefun, t_span, init_conditions, t_eval=t_eval)

# Plot results
plt.figure()
plt.plot(solution.t, solution.y[0], 'r', label='θ (rad)')
plt.plot(solution.t, solution.y[1], 'b', label='θ_dot (rad/s)')
plt.xlabel('Time (s)')
plt.ylabel('State Variables')
plt.title('ODE Solution of Lagrangian System')
plt.legend()
plt.grid()
plt.show()
