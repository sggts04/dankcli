from PIL import Image, ImageFont, ImageDraw
import math
import os
import datetime

TOP_PADDING = 10
BOTTOM_PADDING = 10
MINIMUM_FONT_SIZE = 13 # Lower Bound for font size
HW_ASPECT_RATIO_THRESHOLD = 1.666 # To check if image is highly vertical
WIDTH_PADDING = 5 # To make sure text isn't at complete edge

def getFontSize(img):
    width, height = img.size[0], img.size[1]
    tempSize = max(math.floor(height/13), MINIMUM_FONT_SIZE)
    if tempSize==MINIMUM_FONT_SIZE or not height/width >= HW_ASPECT_RATIO_THRESHOLD:
        # Horizontal or Lower-Bound
        return tempSize
    else:
        # Vertical
        return math.floor(tempSize/1.5)

def getTopLeftCorner(draw, lines, font, img):
    # Align according to longest line
    line = max(lines.split('\n'), key= lambda x: font.getsize(x)[0])
    w= draw.textsize(line, font=font)[0]
    W = img.size[0]
    # Center horizontally, top vertically
    return ((W-w)/2, TOP_PADDING)

# Text wrapper function to wrap text to new line if line gets longer than image width
def textWrap(text, font, max_width):
    lines = []

    if font.getsize(text)[0] < max_width:
        lines.append(text) 
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while line's width is shorter than image width
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] < max_width - WIDTH_PADDING:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)    
    return '\n'.join(lines)

def getWhiteSpaceHeight(lines, font):
    lineNos = len(lines.split('\n'))
    heightPerLine = font.getsize(lines.split('\n')[0])[1]
    # + 20 for 10 padding each for both top and bottom
    return heightPerLine*lineNos + TOP_PADDING + BOTTOM_PADDING

def getFileName():
    currentDateTime = str(datetime.datetime.now()).replace(" ", "").replace("-", "").replace(":", "").replace(".", "")
    return currentDateTime