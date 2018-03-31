# Pixelated
This program requires the python packages PILLOW and pygame
Pixelated is a program that pixelates a given image with a given pixel size. The new image is displayed and saved as "pixel-" + file name. Two examples of the process have been provided in this repository. Galaxy.jpg was processed with a pixel size of 5, and thesun.jpg was processed with a pixel size of 20. 

The algorithm for this program is using the averages of the colors inside each new pixel and setting that as the new color. It works for every positive integer, although pixel size 1 will result in the original image.
