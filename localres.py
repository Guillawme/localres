#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mrcfile as mrc
import numpy as np
import matplotlib.pyplot as plt
import click

# Building blocks

def load_data(mrc_file):
    """Takes an MRC file and returns its data array."""
    with mrc.open(mrc_file) as my_file:
        my_data = my_file.data
    return my_data

def compute_values(relion_locres_mrc, mask_mrc):
    """Takes the MRC data arrays of a local resolution map and a mask, returns local resolution values of all map voxels within the mask."""
    locres = load_data(relion_locres_mrc)
    mask = load_data(mask_mrc)
    values = np.reshape(locres[mask > 0.5], -1)
    return values

def build_histogram(values, title, nbins):
    """Builds a histogram of local resolution values."""
    fig, ax = plt.subplots()
    ax.hist(values, bins = nbins)
    ax.set_xlabel('Local resolution (Å)')
    ax.set_ylabel('Number of map voxels')
    ax.set_title(title)
    ax.grid(True)
    fig.tight_layout()
    return fig

# Command-line tool made from the buidling blocks

@click.command(context_settings = dict(help_option_names = ['-h', '--help']))
@click.argument('relion_locres', metavar = '<relion_locres.mrc>')
@click.argument('mask', metavar = '<mask.mrc>')
@click.option('-t', '--title', 'title', default = '', help = 'Title of the histogram (default: no title).')
@click.option('-b', '--bins', 'nbins', default = 100, type = int, help = 'Number of bins in the histogram (default: 100).')
@click.option('-o', '--output', 'output_file', default = '', help = 'File name to save the histogram (optional: with no file name, simply display the histogram on screen without saving it; recommended file formats: .png, .pdf, .svg or any format supported by matplotlib).')
def cli(relion_locres, mask, title, nbins, output_file):
    """Plots a histogram of local resolution values from a local resolution map and a mask both produced by RELION.

    For meaningful results, the mask.mrc file must be the one used for the 3D refinement and post-processing jobs that produced the relion_locres.mrc file."""
    values = compute_values(relion_locres, mask)
    histogram = build_histogram(values, title, nbins)
    if output_file:
        histogram.figsize = (11.80, 8.85)
        histogram.dpi = 300
        plt.savefig(output_file)
    else:
        plt.show()

if __name__ == '__main__':
    cli()
