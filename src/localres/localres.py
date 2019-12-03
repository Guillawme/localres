#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mrcfile as mrc
import numpy as np
import matplotlib.pyplot as plt

def load_data(mrc_file):
    with mrc.open(mrc_file) as my_file:
        my_data = my_file.data
    return my_data

def compute_values(relion_locres_mrc, mask_mrc):
    locres = load_data(relion_locres_mrc)
    mask = load_data(mask_mrc)
    values = np.reshape(locres[mask > 0.5], -1)
    return values

def plot_histogram(values, title = 'Dataset 1'):
    fig, ax = plt.subplots()
    ax.hist(values, bins = 100)
    ax.set_xlabel('Local resolution (Å)')
    ax.set_ylabel('Number of map voxels')
    ax.set_title(title)
    ax.grid(True)
    plt.show()
    return fig
