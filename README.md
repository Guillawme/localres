# localres

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3575229.svg)](https://doi.org/10.5281/zenodo.3575229)

Plot the histogram of local resolution values of a cryo-EM reconstruction.

From a cryo-EM reconstruction, one can calculate local resolution and generate a
color-coded 3D map showing local resolution across the 3D reconstruction (or
within slices of it). This command-line tool complements this by allowing one to
quantitatively answer the question "how many map voxels inside the mask have a
given local resolution?". This tool generates a histogram of local resolution
values from a local resolution map and a mask (`relion_locres.mrc` and
`mask.mrc` files from RELION, respectively; `cryosparc_*_map_locres.mrc` and
`cryosparc_*_volume_mask_refine.mrc` from cryoSPARC, respectively).

## FAQ

**Q:** Doesn't RELION already do this?

**A:** Yes, RELION-3.1 already prints out this histogram. This tool, however,
doesn't require an installation of RELION, allowing one to inspect files quickly
from a different computer. This tool also lets you adjust the number of bins in
the histogram, and save the histogram as an SVG file (which is useful for
adjusting styling to make a pretty figure).

**Q:** Doesn't cryoSPARC already do this?

**A:** Yes, cryoSPARC already prints out this histogram. This tool, however,
doesn't require an installation of cryoSPARC, allowing one to inspect files
quickly from a different computer. This tool also lets you adjust the number of
bins in the histogram, and save the histogram as an SVG file (which is useful
for adjusting styling to make a pretty figure).

**Q:** Will it work with MRC files produced by my favorite software (not RELION
or cryoSPARC)?

**A:** If these MRC files have the same structure, then yes. But I don't know
for sure, because this tool has only been tested with files produced by RELION
and cryoSPARC.

## Acknowledgments

I would not have been able to put this tool together without the
[`mrcfile`](https://github.com/ccpem/mrcfile) library.

I reused code suggested by
[@biochem_fan](https://twitter.com/biochem_fan/status/1161347681110962177). My
contribution was simply to package it into a command-line tool that's documented
and easy to install.

## Installation

```
$ pip install localres
```

## Usage

```
$ localres --help
Usage: localres [OPTIONS] <relion_locres.mrc> <mask.mrc>

  Plot a histogram of local resolution values from a local resolution map
  and a mask both produced by RELION.

  For meaningful results, the mask.mrc file must be the one used for the 3D
  refinement and post-processing jobs that produced the relion_locres.mrc
  file.

Options:
  -t, --title TEXT    Title of the histogram (default: no title).
  -b, --bins INTEGER  Number of bins in the histogram (default: 100).
  -o, --output TEXT   File name to save the histogram (optional: with no file
                      name, simply display the histogram on screen without
                      saving it; recommended file formats: .png, .pdf, .svg or
                      any format supported by matplotlib).

  -h, --help          Show this message and exit.
```
