import os
import sys
# sys.path.insert(1, r'G:\My Drive\python projects\basic v0')
sys.path.insert(1, os.path.split(os.path.split(os.getcwd())[0])[0])
sys.path.insert(2, os.path.split(os.getcwd())[0])
import basic_plot
import matplotlib.pyplot as plt


basic_plot.figure_parameters.use_default_parameters('small')

basic_plot.figure_parameters.set_font('Times New Roman')

# set figure size and dpi
basic_plot.figure_parameters.set_figure_size(24, 12)
basic_plot.figure_parameters.set_dpi(100)
basic_plot.figure_parameters.see_parameters()
plt.savefig('24x12@100dpi.png')
# it is possible to change dpi when saving
plt.savefig('24x12@100dpi_saved_@200dpi.png', dpi = 200)
plt.savefig('24x12@100dpi_saved_@600dpi.png', dpi = 600)

# increase dpi but not changing figure size -> 
# figure size changes, but once saved will have the same dimension but more resolution
basic_plot.figure_parameters.set_dpi(200)
basic_plot.figure_parameters.see_parameters()
plt.savefig('24x12@200dpi.png')
# it is possible to change dpi when saving
plt.savefig('24x12@200dpi_saved_@100dpi.png', dpi = 100)

basic_plot.figure_parameters.set_dpi(600)
basic_plot.figure_parameters.see_parameters()
plt.savefig('24x12@600dpi.png')
# it is possible to change dpi when saving
plt.savefig('24x12@600dpi_saved_@100dpi.png', dpi = 100)


plt.tight_layout()
plt.show()