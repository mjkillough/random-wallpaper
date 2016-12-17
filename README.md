# random-wallpaper

A very simple script to maintain a collection of random wallpapers in a directory. Call with no arguments (or `--download`) to download a new wallpaper to the directory. Call with `--get` to return the path to a random wallpaper.

Full usage:

```
usage: random_wallpaper.py [-h] [--download | --get]

Maintain a collection of random wallpapers.

optional arguments:
  -h, --help  show this help message and exit
  --download  Download a new wallpaper for later use. (default)
  --get       Return the path to a random wallapper.
```


## License

MIT


## Installing

Install non-Python dependencies (see below) and then: `python setup.py install`.

Arch users can use [this PKGBUILD](https://github.com/mjkillough/arch-packages/tree/master/random-wallpaper).


## Dependencies

Developed/run on Python 3. It should be possible to get it to run on Python 2 with some simple tweaks (if it doesn't already).

Depends on Python packages:

- `requests`
- `xdg`

... these are in `requirements.txt` as usual.


## Developing

The usual:

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python setup.py develop
```

and then run `random-wallpaper` to test your changes.


## Tests

None. Sorry, the script works for me and I haven't had a need to tweak it. If I'm bored I'll come back and add some.


## Acknowledgements

Gets the wallpapers from the wonderful https://unsplash.com.
