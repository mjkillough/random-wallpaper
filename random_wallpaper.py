#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import random
import tempfile

import xdg
import requests


WALLPAPER_URL = 'https://source.unsplash.com/random/2560x1600'
WALLPAPER_DIRECTORY = os.path.join(xdg.XDG_DATA_HOME, 'random-wallpapers')

ACTION_DOWNLOAD = 'download'
ACTION_GET = 'get'


def ensure_directory_exists():
    if os.path.exists(WALLPAPER_DIRECTORY):
        if not os.path.isdir(WALLPAPER_DIRECTORY):
            raise Exception('Expected %s to be a directory' % directory)
        return
    os.makedirs(WALLPAPER_DIRECTORY)


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

    ensure_directory_exists()
    if args.action == ACTION_DOWNLOAD:
        download()
    else:
        print(get())
