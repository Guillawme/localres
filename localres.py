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
    fig.figsize = (11.80, 8.85)
    fig.dpi = 300
    return fig

# Command-line tool made from the buidling blocks

CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

@click.command(context_settings = CONTEXT_SETTINGS)
@click.argument('relion_locres', metavar = '<relion_locres.mrc>')
@click.argument('mask', metavar = '<mask.mrc>')
def cli(relion_locres, mask):
    """Plots a histogram of local resolution values from RELION files.

    For meaningful results, the mask.mrc file must be the one used for the 3D refinement and post-processing jobs that produced the relion_locres.mrc file."""
    values = compute_values(relion_locres, mask)
    plot_histogram(values)

if __name__ == '__main__':
    cli()
