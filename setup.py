#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup


setup(
    name='random-wallpaper',
    description='Script to maintain a collection of random wallpapers.',
    version='1.0',
    author='Michael Killough',
    author_email='michaeljkillough@gmail.com',
    url='https://github.com/mjkillough/random-wallpaper',
    platforms=['linux'],
    license=['MIT'],
    install_requires=[
        'requests',
        'pyxdg'
    ],

    py_modules=['random_wallpaper'],
    entry_points = {
        'console_scripts': [
            'random-wallpaper=random_wallpaper:main',
        ],
    }
)
