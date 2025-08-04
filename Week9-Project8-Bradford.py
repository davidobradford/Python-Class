"""
Program: Week9-Project8-Bradford.py
Author: David Bradford
Due Date: 07/22/25
Semester: Spring 2025
Instructor: Mark Pranger
Function to convert a color image to sepia.
"""
from images import Image

def sepia(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            image.setPixel(x, y, (red, green, blue))

def main():
    image = Image("smokey.gif")
    sepia(image)
    image.draw()

if __name__ == "__main__":
    main()

