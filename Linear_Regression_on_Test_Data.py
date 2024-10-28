import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

filepath = "Test Data/MaxRadiusTestData.csv" #set path to the csv file 
test_data = pd.read_csv(filepath)

x_blue = np.array((test_data['Blue x Values']))
y_blue = np.array((test_data['Blue y Values']))

radius_of_mass_2 = np.max(y_blue) - 5

# Plot the original data
plt.scatter(x_blue, y_blue, color='blue', label='Original Test Data')

# Add labels and title
plt.xlabel('x cm')
plt.ylabel('y cm')
plt.legend()

# Ensure the axis scales are constant
plt.axis('equal')

# Show the plot
plt.show()

# Reshape x_blue for sklearn
x_blue = x_blue.reshape(-1, 1)

# Define the range of polynomial degrees to test
degrees = range(1, 20)

# Initialize lists to store the results
r2_list = []

# Initialize the model
model = LinearRegression(fit_intercept=True)

# Loop over different polynomial degrees
for degree in degrees:
    # Train the model with the best polynomial degree
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(x_blue)
    model.fit(X_poly, y_blue)
    y_pred = model.predict(X_poly)
    
    # Perform cross-validation and calculate the R2 score
    r2 = r2_score(y_blue, y_pred)
    # Append the results to the lists
    r2_list.append(r2)

# Plot the R2 score for different polynomial degrees
plt.plot(degrees, r2_list, marker='o')
plt.xlabel('Polynomial Degree')
plt.ylabel('R-squared Score')
plt.title(f'R2 Score vs Polynomial Degree with\nRadius of second mass: {radius_of_mass_2:.2f} cm')

plt.show()


# Find the best polynomial degree based on MSE
best_degree = degrees[np.argmax(r2_list)]
print(f"Best polynomial degree based on r2: {best_degree}")

# Train the model with the best polynomial degree
poly = PolynomialFeatures(best_degree)
X_blue_poly = poly.fit_transform(x_blue)
model = LinearRegression(fit_intercept=True)
model.fit(X_blue_poly, y_blue)
y_pred = model.predict(X_blue_poly)

# Plot the original data and the predicted data
plt.scatter(x_blue, y_blue, color='blue', label='Original Test Data')
plt.plot(x_blue, y_pred, color='red', label='Predicted Data')

# Add labels and title
plt.xlabel('x cm')
plt.ylabel('y cm')
plt.legend()
plt.title(f'Regression on Test Data with\nRadius of second mass: {radius_of_mass_2:.2f} cm')

# Ensure the axis scales are constant
plt.axis('equal')

# Show the plot
plt.show()


# Calculate and print the MSE and R2 score for the best model
mse_y_pred = mean_squared_error(y_blue, y_pred)
r2_y_pred = r2_score(y_blue, y_pred)

print("\n")
print(f"MSE for best model: {mse_y_pred}")
print(f"R2 score for best model: {r2_y_pred}")