#!/usr/bin/env python3
"""
Change your wallpaper with a random image from Unsplash in a command
"""

__author__ = "Alessio Scarfone"
__version__ = "0.1.0"
__license__ = "MIT"
# ____________________________________________

import json
import os
import argparse
import urllib.request as req
import datetime
import ctypes

now = datetime.datetime.now()

class Configuration:
    preferred_image_size_w = "1920"
    preferred_image_size_h = "1080"
    folder = "."

CONFIGURATION_JSON = "./config.json"

def main(args):
    # Default parameter
    conf = Configuration()

    if args.configure == True:
        create_configuration_json(conf)
    
    if os.path.isfile(CONFIGURATION_JSON) and os.access(CONFIGURATION_JSON, os.R_OK):
        conf.folder,conf.preferred_image_size_w,conf.preferred_image_size_h = get_folder()

    # print(folder + "\n"+ preferred_image_size_w + "\n"+ preferred_image_size_h)
    complete_path = download_img(args.tags,args.daily,conf)
    set_background(complete_path)
    
    if args.end_check == True:
        check_choice(complete_path)


# _______________________________________________________________

def check_choice(complete_path):
    choice = input("Do you like it? (y/n):\t")
    if len(choice) == 0:
        choice = "y"
    while choice.lower() != "y" and choice.lower() != "yes" and choice.lower() != "n" and choice.lower() != "n":
        choice = input("Do you like it? (y/n):\t")

    if choice.lower() == "n" or choice.lower() =="no":
        print ("Deleted....")
        os.remove(os.path.abspath(complete_path))
            

def create_configuration_json(conf):
    conf.folder = input(" >>> Folder used for save image:  ")
    conf.preferred_image_size_w = input(" >>> Preferred Size for the image: \n\twidth:  ")
    conf.preferred_image_size_h = input(" \theight:  ")

    data = {
        "folder": conf.folder,
        "width": conf.preferred_image_size_w,
        "height": conf.preferred_image_size_h
    }
    with open('config.json', 'w') as outfile:
        json.dump(data, outfile)
    print("Configuration json created.")


def get_folder():
    with open(CONFIGURATION_JSON) as json_data_file:
        data = json.load(json_data_file)
        return data['folder'], data['width'], data['height']


def download_img(tags,daily,conf):
    url = "https://source.unsplash.com/"+conf.preferred_image_size_w+"x"+conf.preferred_image_size_h+"/"
    if daily == True:
        url += "daily"

    elif len(tags) != 0:
        url = url + "?"
        for t in range(0,len(tags)):
            url+=tags[t]
            if(t != len(tags)-1):
                url +=","

    print(url)

    filename = "PySplash_"+now.strftime("%Y%m%d_%H_%M_%S")+".jpg"
    complete_path = conf.folder+"/"+filename
    print("Downloading....")
    req.urlretrieve(url, complete_path)

    return complete_path

def set_background(complete_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(complete_path) , 0)


#_______________________________________________________________________

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--configure", help='create configuration file',action='store_true')
    parser.add_argument("-d", "--daily", help='get daily image',action='store_true')
    parser.add_argument('-t', '--tags',  
        nargs='+',      # one or more parameters 
        type=str,       # /parameters/ are string
        default=[]      # since we're not specifying required.
    )
    parser.add_argument("-e", "--end-check", help='delete image if you do not like',action='store_true')

    # Specify output of "--version"
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)