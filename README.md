[![PyPI version](https://badge.fury.io/py/mollview.svg)](https://badge.fury.io/py/mollview)
![Tests](https://github.com/MetinSa/mollview/actions/workflows/tests.yml/badge.svg)
---


`mollview` is a command line tool for plotting HEALPix maps from fits files. `mollview` wraps `healpy`'s `read_map` and `mollview` functions. Most `mollview` keywords are supported (see [the documentation for mollview](https://healpy.readthedocs.io/en/latest/generated/healpy.visufunc.mollview.html) for more information).

# Installation
`pip install mollview`.

# Examples
```bash
>>> mollview my_map.fits

>>> python -m mollview my_map.fits
```
```bash
>>> mollview --help                           
Usage: mollview [OPTIONS] FILENAME

  Plots a HEALPix map from the commandline given a fits file.

Arguments:
  FILENAME  Name of HEALPIX fits file  [required]

Options:
  --field INTEGER                 Column to read. 0 is I, 1 is Q, and 2 is U
                                  [default: 0]
  --norm TEXT                     Normalization method
  --min FLOAT                     Minimum value
  --max FLOAT                     Maximum value
  --coord <TEXT TEXT>...          Coordinate system  [default: None, None]
  --unit TEXT                     Unit
  --nest / --no-nest              Use NESTED pixel ordering  [default: no-
                                  nest]
  --title TEXT                    Title
  --xsize INTEGER                 Size of the figure  [default: 800]
  --notext / --no-notext          Do not show text  [default: no-notext]
  --cmap TEXT                     Color map
  --cbar / --no-cbar              Show color bar  [default: cbar]
  --save / --no-save              Save the figure  [default: no-save]
  --remove-dip / --no-remove-dip  Remove the dipole  [default: no-remove-dip]
  --gal-cut FLOAT                 Symmetric galactic cut for the
                                  dipole/monopole fit. Removes points in
                                  latitude range [-gal_cut, +gal_cut]
  --remove-mono / --no-remove-mono
                                  Remove the monopole  [default: no-remove-
                                  mono]
  --badcolor TEXT                 Color of bad pixels  [default: gray]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```