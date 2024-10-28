import numpy as np
import matplotlib.pyplot as plt

# System parameters
m2 = 0.5  # mass of the attached square (kg)
r = 0.5   # distance of the square from the center of the disc (m)
g = 9.81  # gravitational acceleration (m/s^2)

# Define the potential energy function
def potential_energy(theta):
    return m2 * g * r * np.cos(theta)

# Theta values from 0 to 2pi for full rotation
theta_vals = np.linspace(0, 2 * np.pi, 500)

# Compute potential energy values
U_vals = potential_energy(theta_vals)

# Find equilibrium points (0, pi, 2pi, ...)
equilibrium_points = [0, np.pi, 2 * np.pi]
U_eq_points = potential_energy(np.array(equilibrium_points))

# Plot potential energy curve
plt.figure(figsize=(10, 6))
plt.plot(theta_vals, U_vals, label=r'$U(\theta)$', color='blue')
plt.scatter(equilibrium_points, U_eq_points, color='red', zorder=5)

# Annotate the equilibrium points
for i, eq in enumerate(equilibrium_points):
    plt.text(eq, U_eq_points[i], f'  $\\theta = {i}\\pi$', fontsize=12, verticalalignment='bottom')

# Labels and formatting
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(np.pi, color='green', linestyle='--', label='Stable Equilibrium at $\\theta = \pi$')
plt.axvline(0, color='red', linestyle='--', label='Unstable Equilibrium at $\\theta = 0$')
plt.axvline(2*np.pi, color='red', linestyle='--')

plt.title('Potential Energy Curve with Equilibrium Points')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$U(\theta)$ (Joules)')
plt.xticks([0, np.pi, 2 * np.pi], ['0', r'$\pi$', r'$2\pi$'])
plt.legend()
plt.grid(True)
plt.show()
