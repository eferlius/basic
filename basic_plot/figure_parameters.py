# -*- coding: utf-8 -*-
"""
Just an example on how to set parameters for plots
"""
import matplotlib.pyplot as plt
from . import plots
import numpy as np
#%% plot configurations
"""
date: 2023-11-23 15:47:17
note: to create a figure with highest dpi of given dimension, use the following: 
1) set_figure_size of the dimension you want with default dpi (100)
2) use_default_parameters or set_parameters to decide how big the font
3) set_dpi to increase the dpi. The figure will be bigger, no worries

You can now export in png with:
    - dimension of step 1
    - dpi of step 3
"""

def set_figure_size(w = 24, h = 10, unit = 'cm'):
    if unit == 'cm':
        # inch to cm conversion
        w = w/2.54
        h = h/2.54
    elif unit == 'inch':
        pass
    else:
       raise Exception('Expected unit = \'cm\' or \'inch\'') 
    plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]
    plt.rcParams["figure.figsize"] = (w, h)

def set_dpi(dpi):
    plt.rcParams['figure.dpi'] = dpi

def set_font(font_name):
    plt.rcParams['font.family'] = font_name

def set_parameters(main_title, axes_title, axes_labels, legend, x_ticks, y_ticks, text_inside):
    plt.rcParams.update({'font.size': text_inside}) # for text inside figures
    plt.rc('figure', titlesize=main_title) # for main title
    plt.rc('axes', titlesize=axes_title) # for axis titles
    plt.rc('axes', labelsize=axes_labels) # for axes labels
    plt.rc('legend', fontsize = legend)
    plt.rc('xtick', labelsize=x_ticks)
    plt.rc('ytick', labelsize=y_ticks)

def use_default_parameters(type = 'normal'):
    valid_types = ['mini', 'small', 'normal', 'big', 'huge']
    assert type in valid_types, ("valid types are {}. Got {} instead".format(valid_types, type))
    if type == 'mini':
        set_parameters(16,14,12,10,8,8,6)
    if type == 'small':
        set_parameters(20,18,16,14,12,12,10)
    if type == 'normal':
        set_parameters(28,24,22,20,19,19,15)
    if type == 'big':
        set_parameters(34,30,28,26,24,24,20)
    if type == 'huge':
        set_parameters(38,34,32,30,28,28,24)

def see_parameters():
    start = 0
    stop = 100
    step = 1
    x = np.arange(start, stop, step)
    y = np.arange(start, stop, step)+np.random.rand(len(x))*10

    fig, ax = plots.plts([[x,x+5],[x],[],[x,x]],[[y,y],[y],[],[y,y-10]], 
                         mainTitle = 'plt.rc(\'figure\', titlesize=__)]', 
                         listLegLabels = ['', '', 
                                          'legend [plt.rc(\'legend\', fontsize = __)]',
                                          '',
                                          'legend [plt.rc(\'legend\', fontsize = __)]',
                                          'legend [plt.rc(\'legend\', fontsize = __)]'], 
                         listOfkwargs = [{'color': 'C4'}, {'color' : 'C2'}], 
                         sharex = True, sharey = True, 
                         listTitles = ['axes_title [plt.rc(\'axes\', titlesize=__)]']*4,
                         listXlabels=['axes_labels [plt.rc(\'axes\', labelsize=__)]'],
                         listYlabels=['axes_labels [plt.rc(\'axes\', labelsize=__)]'],)
    
    ax[1,0].text(40, 40, 'text_inside [plt.rcParams.update({\'font.size\': __})]',ha = 'center')
    ax[1,0].text(40, 0,  'x_ticks [plt.rc(\'xtick\', labelsize=__)]',ha = 'center')
    ax[1,0].text(0, 60,  'y_ticks [plt.rc(\'ytick\', labelsize=__)]',ha = 'center')
