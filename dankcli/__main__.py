from PIL import Image, ImageFont, ImageDraw
from .functions import getFontSize, getTopLeftCorner, getWhiteSpaceHeight, textWrap
import os
import argparse

# Parsing Arguments to get Image Path and Meme Text
parser = argparse.ArgumentParser()
parser.add_argument("img", help="relative path to image",
                    type=str)
parser.add_argument("text", help="text to put above image",
                    type=str)
args = parser.parse_args()

whiteColor = 'rgb(255, 255, 255)'
blackColor = 'rgb(0, 0, 0)'
img = Image.open(args.img)
W, H = img.size
line = args.text.replace('\\n', '\n')
font = ImageFont.truetype('fonts/arial.ttf', size=getFontSize(img))

# Check if intentional line-breaks done
if '\n' in line:
    # If yes, individually text wrap every line
    lineslist = []
    newlines = line.split('\n')
    for newl in newlines:
        lineslist.append(textWrap(newl, font, W))
    lines = '\n'.join(lineslist)
else:
    # If not, just text wrap on entire thing
    lines = textWrap(line, font, W)

img2 = Image.new("RGBA",( W, H + getWhiteSpaceHeight(lines, font) ),whiteColor)
img2.paste(img, (0, getWhiteSpaceHeight(lines, font)))
draw = ImageDraw.Draw(img2)

draw.text(getTopLeftCorner(draw, lines, font, img2), lines, fill=blackColor, font=font, align="left")

if not os.path.exists(os.path.join(os.getcwd(), 'dankcli-output')):
    os.mkdir('dankcli-output')
# Get index of new meme for saving
try:
    temp = max([int(i.split('.')[0][4:]) for i in os.listdir(os.path.join(os.getcwd(), 'dankcli-output'))])
except:
    temp = 0

img2.save(f'dankcli-output/meme{temp+1}.png')