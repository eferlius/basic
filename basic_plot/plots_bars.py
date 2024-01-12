import matplotlib.pyplot as plt
import numpy as np
from . import general

def compare_bar_plots(df_list, mean_col_name, std_col_name, x_list, 
                      label_list = [], mainTitle = '', axisTitle = '', capsize = 5, alpha = 0.5, rotation = 'vertical', add_text = True):
    n = len(df_list)
    bar_width = 0.8/n
    offsets = np.linspace(-(n-1)/2,(n-1)/2,n)
    index = range(len(df_list[0]))

    put_legend = True
    if label_list == []:
        label_list = ['']*n
        put_legend = False

    fig, ax = general.create_sub_plots(1, mainTitle = mainTitle, listTitles=[])
    for df, o, l in zip(df_list, offsets, label_list):
            ax[0][0].bar(index + o * bar_width, df[mean_col_name], yerr=df[std_col_name], label = l, capsize=capsize, width=bar_width, alpha = alpha)
            if add_text:
                 for i in index:
                    ax[0][0].text(i + o * bar_width, df[mean_col_name].iloc[i]*0.9, df[mean_col_name].iloc[i], ha = 'center')
    ax[0][0].set_xticks(index, x_list, rotation = rotation)
    if put_legend:
        ax[0][0].legend()
    ax[0][0].grid(True)
    plt.tight_layout()

    return fig, ax