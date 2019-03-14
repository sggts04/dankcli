from PIL import Image, ImageFont, ImageDraw
import math
import os


def getFontSize(img):
    imgSize = img.size
    return math.floor(imgSize[1]/13)

def getTopLeftCorner(draw, lines, font, img):
    # Align according to longest line
    line = max(lines.split('\n'), key=len)
    w= draw.textsize(line, font=font)[0]
    W = img.size[0]
    # Center horizontally, top vertically
    return ((W-w)/2, 10)

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
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
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
    return heightPerLine*lineNos + 20
