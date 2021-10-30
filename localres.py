import mrcfile as mrc
import numpy as np
import matplotlib.pyplot as plt
import click

# Building blocks

def is_mask(mrc):
    """Check whether a given MRC file is a mask."""
    return mrc.header['dmax'] == 1.0

def compute_values(locres, mask):
    """Take MRC files of a local resolution map and a mask, then from their data arrays return local resolution values of all map voxels within the mask."""
    return np.reshape(locres.data[mask.data > 0.5], -1)

def build_histogram(values, title, nbins):
    """Build a histogram of local resolution values."""
    fig, ax = plt.subplots()
    ax.hist(values, bins = nbins)
    ax.set_xlabel('Local resolution (Å)')
    ax.set_ylabel('Number of map voxels')
    ax.set_title(title)
    ax.grid(True)
    fig.tight_layout()
    return fig

# Command-line tool made from the buidling blocks

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('file1', metavar='<relion_locres.mrc>')
@click.argument('file2', metavar='<mask.mrc>')
@click.option('-t', '--title', 'title', default='', help='Title of the histogram.')
@click.option('-b', '--bins', 'nbins', default=100, show_default=True, type=int, help='Number of bins in the histogram.')
@click.option('-o', '--output', 'output_file', default='', help='File name to save the histogram (optional: with no file name, simply display the histogram on screen without saving it; recommended file formats: .png, .pdf, .svg or any format supported by matplotlib).')
def cli(file1, file2, title, nbins, output_file):
    """Plot a histogram of local resolution values from a local resolution map and a mask both produced by RELION.

    For meaningful results, the mask.mrc file must be the one used for the 3D refinement and post-processing jobs that produced the relion_locres.mrc file.
    Files can be passed in any order and will be correctly recognized as the mask and local resolution values."""
    A = mrc.open(file1)
    B = mrc.open(file2)
    if is_mask(A):
        locres = B
        mask = A
    else:
        locres = A
        mask = B
    values = compute_values(locres, mask)
    histogram = build_histogram(values, title, nbins)
    if output_file:
        histogram.figsize = (11.80, 8.85)
        histogram.dpi = 300
        plt.savefig(output_file)
    else:
        plt.show()
    locres.close()
    mask.close()
    A.close()
    B.close()
