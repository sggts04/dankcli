from PIL import Image, ImageFont, ImageDraw
from .functions import getFontSize, getTopLeftCorner, getWhiteSpaceHeight, textWrap, getFileName
import os
import argparse
import sys

# Parsing Arguments to get Image Path and Meme Text
parser = argparse.ArgumentParser()
parser.add_argument("img", help="relative path to image",
                    type=str)
parser.add_argument("text", help="text to put above image",
                    type=str)
# parser.add_argument("-f", "--filename", help="file name for final image", 
#                    type=str)
args = parser.parse_args()

# Checking for JPEG/JPG Image to make sure to later save it as RGB and not RGBA
args_img_lower = args.img.lower()
is_jpeg = True if ("jpg" in args_img_lower or "jpeg" in args_img_lower) else False

whiteColor = "rgb(255, 255, 255)"
blackColor = "rgb(0, 0, 0)"

# Check if specified image exists
try:
    img = Image.open(args.img)
except Exception as e:
    print("Specified image doesn't exist or can't be opened")
    sys.exit(2)

Width, Height = img.size
line = args.text.replace("\\n", "\n")
font_path = os.path.join(os.path.dirname(__file__), "fonts", "arial.ttf")
font = ImageFont.truetype(font_path, size=getFontSize(img))

# Check if intentional line-breaks done
if "\n" in line:
    # If yes, individually text wrap every line
    linesList = []
    intentionalNewLines = line.split("\n")
    for intentionalNewLine in intentionalNewLines:
        linesList.append(textWrap(intentionalNewLine, font, Width))
    lines = "\n".join(linesList)
else:
    # If not, just text wrap on entire thing
    lines = textWrap(line, font, Width)

imageWithWhiteSpace = Image.new("RGBA",( Width, Height + getWhiteSpaceHeight(lines, font) ),whiteColor)
imageWithWhiteSpace.paste(img, (0, getWhiteSpaceHeight(lines, font)))
draw = ImageDraw.Draw(imageWithWhiteSpace)

draw.text(getTopLeftCorner(draw, lines, font, imageWithWhiteSpace), lines, fill=blackColor, font=font, align="left")

# Get name of new image for saving
newName = getFileName()

if is_jpeg:
    rgbImage = imageWithWhiteSpace.convert("RGB")
    rgbImage.save(f"{newName}.jpg")
    print("Saved as " + f"{newName}.jpg")
else:
    imageWithWhiteSpace.save(f"{newName}.png")
    print("Saved as " + f"{newName}.png")
