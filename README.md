# dankcli
[![PyPI version](https://img.shields.io/pypi/v/dankcli.svg?label=PyPI)](https://pypi.org/project/dankcli/)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/dankcli)](https://pepy.tech/project/dankcli)

dankcli is a CLI Image Captioning Tool or Meme Generator which automatically adds white space and text to the top of your image.

## Installation

```bash
$ pip install dankcli
```

## Usage

```bash
$ python -m dankcli [-f "file_name_without_extension"] "path/to/image" "Meme text you want to add"
```

The text gets automatically wrapped according to width of image but you can also have intentional \n in your text.
The image is saved in the current folder with the name as the current date and time, the name can be changed with the optional `-f` or `--filename` argument, specifying a file name without the file extension. 

## Example

#### Example 1 (showing \n functionality)
```bash
$ python -m dankcli "templates/yesbutno.jpg" "Mom at 2am: Are you awake?\n\nMe:"
```
turns this

![](https://i.imgur.com/nW3XPkF.jpg)

to this

![](https://i.imgur.com/h6qgp9m.png)

#### Example 2 (showing auto textwrap)
```bash
$ python -m dankcli "mymemes/helpmeme.jpg" "When you make a meme generator but now you can't stop making memes"
```
turns this

![](https://i.imgur.com/6CDBFwF.jpg)

to this

![](https://i.imgur.com/lSBUfNb.png)

