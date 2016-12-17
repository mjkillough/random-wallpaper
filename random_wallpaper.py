#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import random
import tempfile

import xdg.BaseDirectory
import requests


WALLPAPER_URL = 'https://source.unsplash.com/random/2560x1600'
WALLPAPER_DIRECTORY = xdg.BaseDirectory.save_cache_path('random-wallpaper')

ACTION_DOWNLOAD = 'download'
ACTION_GET = 'get'



def download():
    """Downloads a new wallpaper."""
    resp = requests.get(WALLPAPER_URL)
    resp.raise_for_status()
    with tempfile.NamedTemporaryFile(dir=WALLPAPER_DIRECTORY, delete=False) as f:
        f.write(resp.content)


def get():
    """Gets a random wallpaper from the directory."""
    random_filename = random.choice(os.listdir(WALLPAPER_DIRECTORY))
    return os.path.join(WALLPAPER_DIRECTORY, random_filename)


def main():
    parser = argparse.ArgumentParser(description='Maintain a collection of random wallpapers.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--download', action='store_const', dest='action', const=ACTION_DOWNLOAD,
                       help='Download a new wallpaper for later use. (default)')
    group.add_argument('--get', action='store_const', dest='action', const=ACTION_GET,
                       help='Return the path to a random wallapper.')
    parser.set_defaults(action=ACTION_DOWNLOAD)

    args = parser.parse_args()

    if args.action == ACTION_DOWNLOAD:
        download()
    else:
        print(get())


if __name__ == '__main__':
    main()
