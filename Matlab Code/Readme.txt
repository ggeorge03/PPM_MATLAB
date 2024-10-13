Overview

This MATLAB script captures and processes video frames from a webcam to track the movement of blue and red dots. The script calculates the coordinates of the dots, converts them from pixels to centimetres, and plots their paths. The data is also saved to a CSV file for further analysis.

Requirements

	1. MATLAB: Ensure you have MATLAB installed on your system.
	2. Webcam Support: Install the MATLAB Support Package for USB Webcams.
		o You can install it by navigating to Add-Ons > Get Hardware Support Packages in 		MATLAB and searching for "MATLAB Support Package for USB Webcams".
	3. Colour Thresholder App: If the masks need recalibrating for different lighting 	conditions, download the Color Thresholder app from MATLAB's Add-Ons.

Instructions

	1. Setup:
		o Connect your webcam to the computer.
		o Ensure the webcam is recognized by MATLAB. You can check this by				running webcamlist in the MATLAB command window.
	2. Running the Script:
		o Open the script in MATLAB.
		o Run the script by pressing the Run button or 							typing run('NaughtsAndCrosses.py') in the command window.
	3. Recalibrating Masks:
		o The script uses predefined masks (createMaskBLUE and createMaskRED) to detect 		the blue and red dots.
		o If the masks need recalibrating due to different lighting conditions, use the 		Color Thresholder app:
		1. Open the Color Thresholder app in MATLAB.
		2. Load a sample image from the webcam.
		3. Adjust the colour thresholds to create a new mask.
		4. Export the new mask function and replace the 						existing createMaskBLUE and createMaskRED functions in the script.
	4. Output:
		o The script will display the paths of the blue and red dots in a plot.
		o The coordinates and time data will be saved to a CSV file 					named LowestRadiusTestData.csv.

Script Details

	1. Initialization:
		o Clears the workspace, closes all figures, and turns off warnings.
		o Initializes the webcam and sets up parameters for the experiment.
	2. Data Collection:
		o Captures n frames from the webcam.
		o Processes each frame to find the centroids of the blue and red dots.
		o Records the coordinates and the elapsed time for each frame.
	3. Data Processing:
		o Converts the recorded coordinates from pixels to centimetres.
		o Adjusts the coordinates to account for the apparatus dimensions and the wheel 		diameter.
	4. Data Saving:
		o Combines the processed data into a matrix.	
		o Writes the data to a CSV file with appropriate headers.
	5. Plotting:
		o Plots the paths of the blue and red dots.
		o Adds labels, title, legend, and grid to the plot.
		o Ensures the axis scales are constant.
