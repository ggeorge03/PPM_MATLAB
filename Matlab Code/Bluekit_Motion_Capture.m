clc;
clear all;
close all;
warning off;

% Needs this line below when using webcam via USB
% c = webcam(2);
% Use this line if using built-in laptop webcam
c = webcam;
n = 60;
length_of_apparatus_cm = 43;
diameter_of_wheel_cm = 10;
BLUE_coords_matrix = zeros(n, 2);
RED_coords_matrix = zeros(n, 2);
time_matrix = zeros(n, 1);  % Array to store the time of each recorded point

disp('Begin Experiment')
disp('...')
tic;  % Start the timer

for i = 1:n
    e = snapshot(c);
    fBLUE = createMaskBLUE(e);
    %imshowpair(e, fBLUE, 'montage');
    numfBLUE = sum(fBLUE(:) == 1);
    [fBLUE_col, fBLUE_row] = find(fBLUE.');
    fBLUE_coords = [fBLUE_col, fBLUE_row];
    fBLUE_centroid = sum(fBLUE_coords) / numfBLUE;
    BLUE_coords_matrix(i, 1:2) = [fBLUE_centroid];

    fRED = createMaskRED(e);
    %imshowpair(e, fRED, 'montage');
    numfRED = sum(fRED(:) == 1);
    [fRED_col, fRED_row] = find(fRED.');
    fRED_coords = [fRED_col, fRED_row];
    fRED_centroid = sum(fRED_coords) / numfRED;
    RED_coords_matrix(i, 1:2) = [fRED_centroid];

    % Record the elapsed time
    time_matrix(i) = toc;
end
disp('End Experiment')

%fileID = fopen('plot.txt', 'w');
%fprintf(fileID, '%6.2f %12.8f\n', BLUE_coords_matrix.');
%fclose(fileID);

% Assuming coords_matrix is a 2-column matrix where:
% coords_matrix(:,1) are the x values
% coords_matrix(:,2) are the y values

% Extract time and subtract starting offset
time = time_matrix(:,1)
time = time - min(time)

% Extract x and y from the coords_matrix
x_BLUE = BLUE_coords_matrix(:, 1);  % First column for x values
y_BLUE = BLUE_coords_matrix(:, 2);  % Second column for y values

% Extract x and y from the coords_matrix
x_RED = RED_coords_matrix(:, 1);  % First column for x values
y_RED = RED_coords_matrix(:, 2);  % Second column for y values

% calculate the red blue y axis offset 
% (relative height between the red dot and the blue dot)
y_red_blue_offset = ((mean(y_RED) - min(y_BLUE))+(max(y_BLUE) - mean(y_RED)))/2;

% calcualte the red blue x axis offest 
% (relative length between the red dot and the blue dot)
x_red_blue_offset = min(x_RED) - min(x_BLUE);

% Invert the recorded y values
% This is done because the pixels axis origin is in the top left corner
% Our axis origin is in the bottom left corner
y_BLUE = max(y_BLUE) - y_BLUE;
y_RED = mean(y_RED) - y_RED;

% Set x values to start at origin
x_RED = x_RED - min(x_RED);
x_BLUE = x_BLUE - min(x_BLUE);

% Calculate the conversion factor from pixels to cm
length_of_RED_path_pixels = max(x_RED) - min(x_RED);
pixel_to_cm_conversion_factor = (length_of_apparatus_cm - diameter_of_wheel_cm) / length_of_RED_path_pixels;  

% Convert x and y values from pixels to centimeters
x_BLUE = x_BLUE * pixel_to_cm_conversion_factor;
y_BLUE = y_BLUE * pixel_to_cm_conversion_factor;
x_RED = x_RED * pixel_to_cm_conversion_factor;
y_RED = y_RED * pixel_to_cm_conversion_factor;
y_red_blue_offset = y_red_blue_offset * pixel_to_cm_conversion_factor;
x_red_blue_offset = x_red_blue_offset * pixel_to_cm_conversion_factor;

% Correct the height of the red path
y_RED = y_RED + (diameter_of_wheel_cm/2);

% Correct the height of the blue values
y_BLUE = y_BLUE + ((diameter_of_wheel_cm/2) - y_red_blue_offset);

% Correct the length of the red values
x_RED = x_RED + (diameter_of_wheel_cm/2);

% Correct the length of teh blue values
x_red_blue_offset = (diameter_of_wheel_cm/2) - x_red_blue_offset;
if x_red_blue_offset > 0
    x_BLUE = x_BLUE + x_red_blue_offset;
else
    x_BLUE = (x_BLUE + (diameter_of_wheel_cm/2)) - x_red_blue_offset;
end

% Combine all variables into one matrix
combined_data = [x_BLUE, y_BLUE, x_RED, y_RED, time];

% Create the column headers in the order specified
headers = {'Blue x Values', 'Blue y Values', 'Red x Values', 'Red y Values', 'time'};

% Combine headers and data
combined_cell = [headers; num2cell(combined_data)];

% Write to CSV file using writecell (which handles both headers and data)
output_filename = ['LowestRadiusTestData.csv'];
writecell(combined_cell, output_filename);

% Display confirmation
disp(['Data has been written to ', output_filename]);

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