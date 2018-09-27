# PySplash
Change your wallpaper with a random image from Unsplash

Use Unsplash Source:
https://source.unsplash.com/

## How to use:

### Help:

```
> python pysplash.py -h

usage: pysplash.py [-h] [-c] [-d] [-t TAGS [TAGS ...]] [-e] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -c, --configure       create configuration file
  -d, --daily           get daily image
  -t TAGS [TAGS ...], --tags TAGS [TAGS ...]
  -e, --end-check       delete image if you do not like
  -v, --version         show program's version number and exit
```

### Configuration File:
- `-c` option allow the user to create a configuration json where store informations about: folder where save the downloaded images and preferred size 

```
>python pysplash.py -c
 >>> Folder used for save image:  C:\user\username\Pictures
 >>> Preferred Size for the image:
        width:  1920
        height:  1080
Configuration json created.
```
**NOTA:** `config.json` is created and searched in the same folder of the script

### Basic usage:
```
>python pysplash.py
```

### Daily Image:
- `-d` download the daily image

**NOTE:** Daily image has priority over the tag list

### Select image based on Keywords:
- `-t` allow user to select some keyword for select image

```
>python pysplash.py -t water,shark
https://source.unsplash.com/1920x1080/?water,shark
Downloading....
```
**Image that respect "water" and/or "shark" keywords**
![Image that respect "water" and/or "shark" keyword](https://images.unsplash.com/photo-1530512112376-c3928c2ee68a?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1920&h=1080&fit=crop&ixid=eyJhcHBfaWQiOjF9&s=8593a8c832b1808b0558fb1434455df6)

### Automatically delete unwanted images:
- If `-e` option is used, after the download, is requested if delete or not the image

```
>python pysplash.py -d -e
https://source.unsplash.com/1920x1080/daily
Downloading....
Do you like it? (y/n):  n
Deleted....
```



