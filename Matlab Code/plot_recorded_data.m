% Plot x and y in centimeters
figure;
hold on;  % Hold the current plot so that new plots are added to the same figure

% Plot the blue path
plot(x_BLUE, y_BLUE, 'Color', 'b', 'DisplayName', 'Blue Dot Path');

% Plot the red path
plot(x_RED, y_RED, 'Color', 'r', 'DisplayName', 'Red Dot Path');

% Add labels and title
xlabel('X-axis (cm)');
ylabel('Y-axis (cm)');
title('Plot of Blue and Red points');

% Add legend
legend;

% Ensure the axis scales are constant
axis equal;

% Optional: Add grid for better visibility
grid on;

hold off;  % Release the hold on the current plot