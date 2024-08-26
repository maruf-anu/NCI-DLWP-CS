import ipywidgets as widgets
import xarray as xr
import os
from IPython.display import clear_output
from time import sleep
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML
from ipywidgets import IntProgress
from IPython.display import display
import time
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

ds = None

def get_time_list():
    time_list = list( ds['time'].to_numpy() )
    time_list = [str(t)[:13] for t in time_list ]
    return time_list

fig = plt.figure(figsize=(10,5))
fig.tight_layout()
ax1 = plt.subplot(1,2,1)   
ax2 = plt.subplot(1,2,2)

time_select = '2017-01-01T00'

def get_title():
    title_1 = ax1.set_title( 'z_500 '  +
        str(ds ['forecast'].sel(time=time_select)[0][0]["time"].to_numpy())[:13]
                        + ", Fourcast Hour: " +
                        str(ds ['forecast'].sel(time=time_select)[0][0]["f_hour"].to_numpy())
                       )
    title_2 = ax2.set_title( 't2m ' + 
        str(ds ['forecast'].sel(time=time_select)[0][1]["time"].to_numpy())[:13]
                        + ", Fourcast Hour: " +
                        str(ds ['forecast'].sel(time=time_select)[0][1]["f_hour"].to_numpy())
                       )
    return title_1, title_2

def get_plot():
    plot_1 = ax1.imshow(ds ['forecast'].sel(time=time_select)[0][0])    
    plot_2 = ax2.imshow(ds ['forecast'].sel(time=time_select)[0][1])
    return plot_1, plot_2

progress = IntProgress(description='Loading:', min=0, max=19) # instantiate the bar


def drawframe(n):
    #print (time_select)
    progress.value = n
    plot_1.set_data( ds ['forecast'].sel(time=time_select)[n][0])
    plot_2.set_data( ds ['forecast'].sel(time=time_select)[n][1])

    title_1.set_text( 'z_500 '  +
        str(ds ['forecast'].sel(time=time_select)[n][0]["time"].to_numpy())[:13]
                      + ", Fourcast Hour: " +  
                     str(ds ['forecast'].sel(time=time_select)[n][0]["f_hour"].to_numpy())
                    )
    title_2.set_text( 't2m ' + 
        str(ds ['forecast'].sel(time=time_select)[n][1]["time"].to_numpy())[:13]
                      + ", Fourcast Hour: " +  
                     str(ds ['forecast'].sel(time=time_select)[n][1]["f_hour"].to_numpy())
                    )
    return (plot_1,plot_2)
    
def interactive_fun(Time):
    plt.close()
    global time_select
    time_select = Time
    #print (Time, time_select)
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, drawframe, frames=20, interval=250, blit=True)
    return display(HTML(anim.to_jshtml()))
    
#plt.close()   
#display(progress)
#interact(interactive_fun, Time=time_list)