# dankcli

dankcli is a CLI Meme Generator which automatically adds white space and text to the top of your image.

## Installation

```bash
$ pip install dankcli
```

## Usage

```bash
$ python -m dankcli 'path/to/image' 'Meme text you want to add'
```

The text gets automatically wrapped according to width of image but you can also have intentional \n in your text.
The meme is saved in a new folder called 'dankcli-output' with a name 'meme%s.png'

## Example

#### Example 1 (showing \n functionality)
```bash
$ python -m dankcli 'templates/yesbutno.jpg' 'Mom at 2am: Are you awake?\n\nMe:'
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

