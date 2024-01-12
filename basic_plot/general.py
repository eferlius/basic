import numpy as np
import matplotlib.pyplot as plt

from . import _list_operations_

def create_sub_plots(nOfPlots = 0, sharex = False, sharey = False,
                   nrows = 0, ncols = 0, mainTitle = '', listTitles = [''],
                   listXlabels = [''], listYlabels = ['']):
    '''
    Creates a grid of subplots with nOfPlots or nrows and ncols specified

    Parameters
    ----------
    nOfPlots : int, optional
        number of plots to be created, by default 0
    sharex : bool, optional
        how x is shared between axes (True, 'row', 'col', False), 
        by default False
    sharey : bool, optional
        how y is shared between axes (True, 'row', 'col', False), 
        by default False
    nrows : int, optional
        number of rows for subplot, by default 0
    ncols : int, optional
        number of cols for subplot, by default 0
    mainTitle : str, optional
        main title of the plot, by default ''
    listTitles : list, optional
        list of titles of each axis, ordered in a horizontal list as the axes appear. 
        If no title is associated with an axis, use '' as a placeholder, by default ['']
    listXlabels : list, optional
        list of x label of each axis, ordered in a horizontal list as the axes appear. 
        If no x label is associated with an axis, use '' as a placeholder, by default ['']
    listYlabels : list, optional
        list of y label of each axis, ordered in a horizontal list as the axes appear. 
        If no y label is associated with an axis, use '' as a placeholder, by default ['']

    Returns
    -------
    fig : matplotlib figure
        DESCRIPTION.
    ax : 2d array of axes
        It's always a 2d array
    '''

    # detect number of rows and of columns
    if nrows*ncols < nOfPlots and nrows != 0 and ncols != 0:
        nrows = 0
        ncols = 0
    if nrows == 0 and ncols == 0:
        nrows = int(np.ceil(np.sqrt(nOfPlots)))
        ncols = int(np.ceil(nOfPlots/nrows))
    elif nrows == 0 and ncols != 0:
        nrows = int(np.ceil(nOfPlots/ncols))
    elif nrows != 0 and ncols == 0:
        ncols = int(np.ceil(nOfPlots/nrows))
    else:
        pass
        # both ncols and nrows are specified

    # add empty titles in the end if some are missing
    listTitles = _list_operations_.make_list(listTitles)
    listXlabels = _list_operations_.make_list(listXlabels)
    listYlabels = _list_operations_.make_list(listYlabels)
    listTitles.extend(['']*(nOfPlots-len(listTitles)))
    listXlabels.extend(['']*(nOfPlots-len(listXlabels)))
    listYlabels.extend(['']*(nOfPlots-len(listYlabels)))

    # create the figure with subplots
    fig, ax = plt.subplots(nrows, ncols, sharex = sharex, sharey = sharey, squeeze = False)
    plt.suptitle(mainTitle, wrap=True)
            
    ac = -1 #ax counter
    for row in range(nrows):
        for col in range(ncols):
            ac += 1
            if ac >= nOfPlots:
                break
            this_ax = ax[row][col]
            this_ax.set_title(listTitles[ac], wrap=True)
            this_ax.set_xlabel(listXlabels[ac])
            this_ax.set_ylabel(listYlabels[ac])
            this_ax.grid()
    return fig, ax