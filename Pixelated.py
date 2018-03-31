# Created by Tyler Lennen <tlennen@ucmerced.edu>
# The program pixelates a given image, with a given pixel size.
# The new image is displayed and saved as "pixel-" + file name

import pygame
from pygame.locals import *
from PIL import Image

done = False
im = 0
pixel_size = 0
file_name = ""
while not done:
    # takes in the file name, prompts again if file not found
    try:
        file_name = input("Enter the name of an image file: ")
        im = Image.open(file_name)
        done = True
        file_name = "pixel-" + file_name
    except IOError:
        print("File not found. Image must be in the same folder as this program.")

done = False
while not done:
    # Takes in pixel size of image, prompts again if a non-integer
    pixel_size = input("Enter the size of the pixels: ")
    try:
        pixel_size = int(pixel_size)
        done = True
        if pixel_size == 0:
            print("Pixel size cannot equal 0. Enter a valid input.")
            done = False
    except ValueError:
        print("Input was not an integer. Enter a valid input.")


def pixelize(image, blur):
    # takes average color of each pixel in new pixel size
    pix = im.load()
    for x in range(0,int(image.size[0]/blur)+1):
        for y in range(0,int(image.size[1]/blur)+1):
            average = [0, 0, 0]
            count = 0
            # gathers sum of colors of each pixel, in order to take the average
            for i in range(0, blur):
                for j in range(0, blur):
                    if image.size[0] > x*blur+i and image.size[1] > y*blur+j:
                        average[0] += pix[x * blur + i, y * blur + j][0]
                        average[1] += pix[x * blur + i, y * blur + j][1]
                        average[2] += pix[x * blur + i, y * blur + j][2]
                        count += 1
            if count == 0:  # prevents divide by zero error
                count = 1
            average = [average[0]/count, average[1]/count, average[2]/count]
            color = (int(average[0]), int(average[1]), int(average[2]))
            for i in range(0, blur):
                # sets pixels to new color
                for j in range(0, blur):
                    if image.size[0] > x * blur + i and image.size[1] > y * blur + j:
                        pix[x * blur + i, y * blur + j] = color
    im.save(file_name)


pixelize(im, pixel_size)
screen_width = im.size[0]
screen_height = im.size[1]
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('Pixelate')
picture = pygame.image.load(file_name)
pygame.display.set_icon(picture)
screen.blit(picture, (0, 0))  # displays image on screen
pygame.display.flip()

while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        # quits program
        pygame.display.quit()
        break
    elif event.type == VIDEORESIZE:
        # resize image with window
        screen_width, screen_height = event.size
        if screen_width < 100:
            screen_width = 100
        if screen_height < 100:
            screen_height = 100
        screen = pygame.display.set_mode((screen_width, screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(picture, (screen_width,screen_height)), (0, 0))
    pygame.display.flip()
