#!/usr/bin/env python
#GPT helped remove error message 

import sys

import numpy
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def main():
    rapa_data = numpy.loadtxt('WT_NF_Rapa_counts.tsv')
    nf_data = numpy.loadtxt('WT_NF_Ctrl_counts.tsv')
    nf_rep_data = numpy.loadtxt('WT_NF_Ctrl_rep_counts.tsv')

    # The row and column names are stored in separate files. The sampling time and replicate can be extracted from the sample names
    genes = numpy.array([name.rstrip() for name in open('gene_names.txt')])
    sample_labels = numpy.array([name.rstrip().split('\t') for name in open('samples.txt')])
    times = numpy.array([int(time.split('_')[1]) for time, rep in sample_labels if rep == 1], numpy.int32)
    rep_times = numpy.array([int(time.split('_')[1]) for time, rep in sample_labels], numpy.int32)
    reps = numpy.array([int(rep.split('_')[1]) for time, rep in sample_labels], numpy.int32)
    plot_pca(nf_rep_data, rep_times, reps, 'Exercise 1 PCA', 'exercise1_PCA.png')
    #1.3 the reliplicates tend to cluster together and the same colored dots are closeby. But I expected them to be more similar to even more close to each other to form like a circlefor each timepoint.  

    nf_mean = numpy.mean(nf_data, axis=1)
    nf_std = numpy.std(nf_data, axis=1)

    filter = (nf_mean > 0.85) & ((nf_std / nf_mean) > 0.115)

    filtered_nf = nf_data[filter, :]
    filtered_rapa = rapa_data[filter, :]
    filtered_rep = nf_rep_data[filter, :]

    plot_pca(filtered_rep, rep_times, reps, 'Exercise 2.1 PCA', 'exercise2.1_PCA.png')
    #2.1 the new PCA graph looks similar to exercise 1 even after removing low expression values or noise. 

    norm_nf = normalize_data(filtered_nf)

    norm_rapa = normalize_data(filtered_rapa)

    peak = numpy.argmax(norm_nf, axis=1)

    pc1, pc2 = gene_pca(norm_nf,peak, 'Exercise 2.3 PCA','exercise2.3_PCA.png')


    angles = numpy.arctan2(pc2, pc1)

    plot_hm(norm_nf, title='Exercise 3.1', orderby=angles, fname='exercise3.1_heatmap.png')

    aligned_nf = align_times(norm_nf, angles)
    
    aligned_rapa = align_times(norm_rapa, angles)

    plot_hm(aligned_nf, title='Exercise 3.2', fname='exercise3.2_heatmap.png')

    combined = numpy.concatenate((aligned_nf, aligned_rapa), axis=1)

    kmeans = KMeans(n_clusters=6, random_state=42)

    groups = kmeans.fit_predict(combined)

    plot_hm(aligned_nf, aligned_rapa, title='Exercise 3.4',orderby=groups, showgroups=True,fname='exercise3.4_heatmap.png')


def plot_pca(data, times, reps, title, fname):
    pca = PCA(2, random_state=42)
    pcs = pca.fit_transform(data.T)

    plt.figure()
    plt.scatter(pcs[:, 0], pcs[:, 1], c=times, cmap='Set1', s=reps*15)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title(title)
    plt.savefig(fname)
    plt.show()    

def gene_pca(data, colors, title, fname):
    pca = PCA(2, random_state=42)
    pcs = pca.fit_transform(data)

    plt.figure()
    plt.scatter(pcs[:, 0], pcs[:, 1], c=colors, cmap='Set1')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title(title)
    plt.savefig(fname)
    plt.show()

    return pcs[:, 0], pcs[:, 1]

def normalize_data(data):
    """
    Function to normalize data along the second axis of a 2D array.

    Parameters:
    -----------
    data : ndarray
           A 2D matrix containing sample data where the rows are samples and columns are features.

    Returns:
    --------
    norm_data : ndarray
                An array of the sample shape and data type as the original data with values normalized along the second axis.
    """
    norm_data = numpy.copy(data)
    norm_data -= numpy.mean(norm_data, axis=1, keepdims=True)
    norm_data /= numpy.std(norm_data, axis=1, keepdims=True)
    return norm_data


def plot_hm(*data, xlabel='', ylabel='', title='', orderby=None, showgroups=False, fname=None):
    """
    Function for plotting heatmap/matrix style data.

    Parameters:
    -----------
    data : ndarray(s)
           The array or arrays should be 2D with rows plotted along the y-axis and columns plotted along the x-axis.
           If multiple arrays are passed as positional arguments, they need to have the same number of rows.
    xlabel : str
           An x-axis label for the plotted data
    ylabel : str
           A y-axis label for the plotted data
    title : str
           A title to add above the plot
    orderby : ndarray
           A list of indices or group labels for ordering the data along the x-axis. If None, the data order is not changed
    showgroups : bool
           An indicator whether the group labels passed to `orderby` should be plotted as an additional color bar. Ignored if orderby is None.
    fname : str
           A file name to save the plot to. If None, the plot is only displayed but not saved.
    
    Returns:
    --------
    None
    """
    if orderby is None:
        order = numpy.arange(data[0].shape[0])
    else:
        order = numpy.argsort(orderby)
    if orderby is None or not showgroups:
        fig, ax = plt.subplots(1, len(data), figsize=(3, 15))
        if len(data) > 1:
            for i in range(len(data)):
                ax[i].imshow(data[i][order, :], aspect='auto')
                ax[i].set_xlabel(xlabel)
                if i > 0:
                    ax[i].set_yticks([])
            ax[0].set_ylabel(ylabel)
        else:
            ax.imshow(data[0][order, :], aspect='auto')
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
    else:
        groups = orderby[order]
        fig, ax = plt.subplots(1, len(data) + 1, width_ratios=[1] + [3] * len(data), figsize=(4, 15))
        if len(data) > 1:
            for i in range(len(data)):
                ax[i + 1].imshow(data[i][order, :], aspect='auto')
                ax[i + 1].set_xlabel(xlabel)
                ax[i + 1].set_ylabel('')
                ax[i + 1].set_yticks([])
        else:
            ax[-1].imshow(data[0][order, :], aspect='auto')
            ax[-1].set_xlabel(xlabel)
            ax[-1].set_ylabel('')
            ax[-1].set_yticks([])
        ax[-1].yaxis.tick_right()
        ax2 = ax[-1].twinx()
        ax2.set_ylabel(ylabel)
        ax[0].set_ylabel('group')
        ax[0].imshow(groups.reshape(-1, 1), aspect='auto')
        bounds = numpy.r_[0, numpy.where(groups[1:] != groups[:-1])[0] + 1, groups.shape[0]] - 0.5
        ax[0].set_yticks((bounds[:-1] + bounds[1:]) / 2)
        ax[0].set_yticklabels([str(i) for i in range(bounds.shape[0] - 1)])
        ax[0].set_xticks([])
    if title:
        plt.suptitle(title)
    if fname is not None:
        plt.savefig(fname, dpi=300, bbox_inches='tight')
    plt.show()


def align_times(data, angle):
    """
    This function takes a 2D matrix of data and a 1D matrix of angles (radians) and shifts data along the second axis (axis=1)
    to align all rows to have an effective angle of zero.

    Parameters:
    -----------
    data : ndarray
           A 2D matrix of data where each row is a sample and each column is a measurement in a cyclical cycle
    angle : ndarray
           A 1D matrix of data of a length equal to the number of rows in data. Angles should be in radians.
           
    Returns:
    --------
    aligned : ndarray
              A new array with data shifted along the second axis to align each row to have an angle of zero
    """
    n = data.shape[1]
    offsets = n - angle * n / (numpy.pi * 2)
    offsets[numpy.where(offsets < 0)] += n
    aligned = numpy.zeros_like(data)
    for i in range(data.shape[0]):
        aligned[i, :] = (numpy.roll(data[i, :], int(numpy.floor(offsets[i]))) * (numpy.ceil(offsets[i]) - offsets[i]) +
                         numpy.roll(data[i, :], int(numpy.ceil(offsets[i]))) * (offsets[i] - numpy.floor(offsets[i])))
    
    return aligned


main()
