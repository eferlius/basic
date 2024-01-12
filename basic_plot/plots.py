# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:38:34 2022

@author: eferlius
"""
#%% imports
import matplotlib.pyplot as plt
from . import _check_
from . import _list_operations_
from . import general
       
def plts(X = [], Y = [], sharex = False, sharey = False, nrows = 0, ncols = 0, 
mainTitle = '', listTitles = [''], listXlabels = [''], listYlabels = [''], 
listLegLabels = [''], listXlim = [''], listYlim = [''], listOfkwargs = [{}], 
common_kwargs = {'marker': '.'}):
    '''
    Given (X,Y), plots them
    X and Y can be 
    - 1D-list
    - 1D-np.array, 
    - list of 1D-lists
    - list of 1D-np.arrays

    *warning*: if instead of 1D the lists or np.arrays are 2D, it's up to the 
    user resize and transpose them in the correct way

    Assuming xn and yn are either lists or np.arrays, it's possible to obtain:
    - plts(x0,y0) -> one axis: x0y0
    - plts([x0,x1],[y0,y1]) -> two axes: x0y0 and x1y1
    - plts([x0,x1,x2],[y0,y1,y2]) -> three axes: x0y0, x1y1 and x2y2
    - plts([x0,[x1,x2]],[y0,[y1,y2]]) -> two axes: x0y0 and x1y1x2y2
    - plts([[x0,x1]],[[y0,y1]]) -> one axis x0y0x1y1 (mind the double square bracket)

    sharex and sharey allow to define the axis sharing (in case of more than 
    one axis, otherwise it's ignored).

    nrows and ncols allow to decide the layout of the subplot (in case of more 
    than one axis, otherwise it's ignored).

    mainTilte is the title of the plot.

    listTitles is a 1D-list containing the title of each axis.

    listLegLabels and listOfkwargs are 1D-lists containing respectively the label 
    and the kwargs to be applied to each plot. 
    If X and Y are 2D (ex: plts([x0,[x1,x2]],[y0,[y1,y2]]), it's not necessary 
    to follow the same structure to specify labels and kwargs, just use the 1D-list 
    (in this case listLegLabels = [l0, l1, l2] and listOfkwargs = [kw0, kw1, kw2]). 
    If no label for a plot, use '' as a placeholder.
    If no kwargs for a plot, use {} as a placeholder.

    common_kwargs are applied to all the plots, the same parameter can be overwritten 
    by means of the corresponding value in listOfkwargs.  
    
    Parameters
    ----------
    X : list, optional
        list of x arrays, can be list, np.array, list of list or list of 
        np.array, by default []
    Y : list, optional
        list of y arrays, can be list, np.array, list of list or list of 
        np.array, by default []
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
    listLegLabels : list, optional
        list of labels of each plot, ordered in a horizontal list as the plots appear. 
        If no label is associated with a plot, use '' as a placeholder, by default ['']
    listXlim: list, optional
        list of xlim for each plot, ordered in a horizontal list as the plots appear. 
        If no xlim is associated with a plot, use '' as a placeholder, by default ['']
    listYlim: list, optional
        list of ylim for each plot, ordered in a horizontal list as the plots appear. 
        If no ylim is associated with a plot, use '' as a placeholder, by default ['']
    listOfkwargs : list, optional
        list of kwargs of each plot, ordered in a horizontal list as the plots appear. 
        If no kwarg is associated with a plot, use {} as a placeholder,
        by default [{}]
    common_kwargs : dict, optional
        kwarg applied to all the plots, by default {'marker': '.'}      
    
    Returns
    -------
    fig : matplotlib figure
        DESCRIPTION.
    ax : 2d array of axes
        DESCRIPTION.
    '''

    Y = _list_operations_.make_listOfList_or_listOfNpArray(Y)
    nOfPlots = len(Y)

    if _check_.is_emptyList_or_emptyNpArray(X):
        X = [[]] * nOfPlots
    else:
        X = _list_operations_.make_listOfList_or_listOfNpArray(X) 

    listLegLabels = _list_operations_.make_list(listLegLabels)
    listOfkwargs = _list_operations_.make_list(listOfkwargs)
    listXlim = _list_operations_.make_list(listXlim)
    listYlim = _list_operations_.make_list(listYlim)

    fig, ax = general.create_sub_plots(nOfPlots, sharex, sharey, nrows, ncols, mainTitle, 
    listTitles, listXlabels, listYlabels)

    nrows = len(ax)
    ncols = len(ax[0])

    lkc = -1 # listLegLabels and listOfKwargs counter
    ac = -1 #ax counter
    for row in range(nrows):
        for col in range(ncols):
            ac += 1
            if ac >= nOfPlots:
                continue

            this_ax = ax[row, col]
            this_X = _list_operations_.make_listOfList_or_listOfNpArray(X[ac])
            this_Y = _list_operations_.make_listOfList_or_listOfNpArray(Y[ac])
            
            # setting x lim for this axis
            try:
                this_ax_xlim = listXlim[ac] 
                this_ax.set_xlim(this_ax_xlim)
            except: 
                pass
            # setting y lim for this axis
            try:
                this_ax_ylim = listYlim[ac] 
                this_ax.set_ylim(this_ax_ylim)
            except: 
                pass

            tac = -1 #this ax counter
            for x, y in zip (this_X, this_Y):
                lkc += 1
                tac += 1

                this_plt_kwargs = common_kwargs.copy()
                try:
                    this_plt_kwargs.update(listOfkwargs[lkc])
                except:
                    pass
                finally:
                    try:
                        # if label for this plot
                        this_plt_label = listLegLabels[lkc]
                        if this_plt_label == '':
                            raise Exception()
                        if not _check_.is_emptyList_or_emptyNpArray(x):
                            this_ax.plot(x, y, **this_plt_kwargs, label = this_plt_label)
                        else:
                            this_ax.plot(y, **this_plt_kwargs, label = this_plt_label)
                        this_ax.legend()
                    except:
                        # if no label for this plot
                        if not _check_.is_emptyList_or_emptyNpArray(x):
                            this_ax.plot(x, y, **this_plt_kwargs)
                        else:
                            this_ax.plot(y, **this_plt_kwargs)
            
    plt.tight_layout()
    return fig, ax