import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.insert(1, os.path.split(os.path.split(os.getcwd())[0])[0])
sys.path.insert(2, os.path.split(os.getcwd())[0])
import basic_plot
import matplotlib.pyplot as plt
    
start = 0
stop = 100
step = 1
x = np.arange(start, stop, step)
y = np.arange(start, stop, step)+np.random.rand(len(x))*10


fig, ax = basic_plot.plots.plts(x,y, mainTitle = 'plts with one x and y', listLegLabels = 'x+ 0')

fig, ax = basic_plot.plots.plts([x,x+5],[y,y], mainTitle = 'plts with two x and y detatched', 
listLegLabels = ['x + 0', 'x + 5'], listOfkwargs = [{'color': 'C4'}, {}], 
sharex = True, sharey = True, ncols = 2, listTitles = ['here x + 0', 'here x + 5'])

fig, ax = basic_plot.plots.plts([[x,x+5]],[[y,y]], mainTitle = 'plts with two x and y on the same', 
listLegLabels = ['x + 0', 'x + 5'], listOfkwargs = [{'color': 'C4'}, {'color' : 'C2'}], 
sharex = True, sharey = True, listTitles = ['here x + 0 and x + 5'])

fig, ax = basic_plot.plots.plts([[x,x+5], x+10],[[y,y], y], mainTitle = 'plts with two x and y on the same', 
listLegLabels = ['x + 0', 'x + 5', 'x + 10'], 
listOfkwargs = [{'color': 'C4'}, {}, {'color' : 'C2', 'linewidth' : '0', 'markersize' : '10'}], 
sharex = True, sharey = True, ncols = 1, listTitles = ['here x + 0 and x + 5', 'here x + 10'])

fig, ax = basic_plot.plots.plts([[x,x+5], x+10],[[y,y], y], mainTitle = 'plts with two x and y on the same - np.array()', 
listLegLabels = ['', 'x + 5', 'x + 10'], sharex = True, sharey = True, ncols = 1, 
listTitles = ['here x + 0 and x + 5', 'here x + 10'])

fig, ax = basic_plot.plots.plts([[x,x+5], x+10],[[y,y], y], mainTitle = 'plts with two x and y on the same', 
sharex = True, sharey = True, ncols = 1, listTitles = ['here x + 0 and x + 5', 'here x + 10'])

fig, ax = basic_plot.plots.plts([[x,x+5], x+10],[[y,y], y], 
mainTitle = 'plts with two x and y on the same - with x and y labels', 
sharex = True, sharey = True, ncols = 1, listTitles = ['here x + 0 and x + 5', 'here x + 10'], 
listXlabels=['','x'], listYlabels=['couple of y', 'y alone'])

xm = np.array([[1],[2],[3]])
ym = np.array([[4],[6],[5]])

fig, ax = basic_plot.plots.plts(np.squeeze(np.transpose(xm)),np.squeeze(np.transpose(ym)), 
mainTitle = 'use of vertical numpy arrays -> need to transpose them')



img00 = [[[255,0,0],[255,0,0],[0,255,0]],[[0,0,255],[0,0,255],[0,255,0]]]
img01 = [[[255,0,0],[255,0,0],[0,0,0]],[[0,0,255],[0,0,255],[0,0,0]]]
imggray = [[0, 128, 255],[255,128,0]]

basic_plot.plots_image.plts_img([img00, img01, imggray], listTitles=['img00', 'img01','img gray'], 
mainTitle = 'list of lists for RGB image')
basic_plot.plots_image.plts_img([np.array(img00), np.array(img01), np.array(imggray)], 
listTitles=['img00', 'img01','img gray'], mainTitle = 'list of np arrays for RGB image')

basic_plot.plots_image.plts_img([img01], mainTitle = 'list for RGB image with square brackets -> ok')
basic_plot.plots_image.plts_img(img01, mainTitle= 'list for RGB image without square brakets -> not ok')
basic_plot.plots_image.plts_img(np.array(img01), mainTitle= 'np array for RGB image without square brackets -> ok')

basic_plot.plots_image.plts_img([imggray], mainTitle = 'list for gray image with square brackets -> ok')   
# pltsImg(imggray, mainTitle = 'list for gray image without square brackets -> error')
basic_plot.plots_image.plts_img(np.array(imggray), mainTitle = 'np array for gray image without square brackets -> ok')

basic_plot.plots_image.plts_img_color_palette(4)


plt.show()