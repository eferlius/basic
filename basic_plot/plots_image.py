import numpy as np
import matplotlib.pyplot as plt

from . import _list_operations_
from . import general


def plts_img(imgs, sharex = False, sharey = False, nrows = 0, ncols = 0, 
mainTitle = '', listTitles = [''], listXlabels = [''], listYlabels = ['']):
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

    sharex and sharey allow to define the axis sharing (in case of more than one 
    axis, otherwise it's ignored).

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

    common_kwargs are applied to all the plots, the same parameter can be 
    overwritten by means of the corresponding value in listOfkwargs.  
    
    Parameters
    ----------
    X : list, optional
        list of x arrays, can be list, np.array, list of list or list of np.array, by default []
    Y : list, optional
        list of y arrays, can be list, np.array, list of list or list of np.array, by default []
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

    imgs = _list_operations_.make_listOfList_or_listOfNpArray(imgs)
    nOfPlots = len(imgs)

    fig, ax = general.create_sub_plots(nOfPlots, sharex, sharey, nrows, ncols, mainTitle, listTitles, listXlabels, listYlabels)

    nrows = len(ax)
    ncols = len(ax[0])

    ac = -1 #ax counter
    for row in range(nrows):
        for col in range(ncols):
            ac += 1
            if ac >= nOfPlots:
                continue

            this_ax = ax[row, col]
            this_ax.imshow(imgs[ac], interpolation = None)
    plt.tight_layout()
    return fig, ax

def plts_img_color_palette(num = 9):
    imgs = []
    for r in np.linspace(0,num-1,num):
        r = int(r)
        img = np.ones((num,num,3))
        img[:,:,0] = r/(num-1)*255
        for g in np.linspace(0,num-1,num):
            g = int(g)             
            img[g,:,1] = g/(num-1)*255
            for b in np.linspace(0,num-1,num):
                b = int(b)          
                img[g,b,2] = b/(num-1)*255
        imgs.append(img.astype(np.uint8))

    plts_img(imgs, mainTitle = 'RGB Palette', 
    listTitles = ['R:{}'.format(i/(num-1)*255) for i in range(num)], 
    listYlabels = ['G (0->255)']*(num), listXlabels= ['B (0->255)']*(num))