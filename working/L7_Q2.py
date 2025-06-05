import numpy as np
import matplotlib.pyplot as plt




def myplot(a_func):

    def wrapTheFunction():
        
        from cycler import cycler
        from matplotlib import rc
        rc('font', family='serif', size=14)
        rc('lines', linewidth=5, color='r')
        rc('axes', prop_cycle=cycler('color', ['r']))
        rc('text', usetex=False) 
        rc('figure',max_open_warning=1000)
        rc('xtick',top=True)
        rc('ytick',right=True)
        rc('ytick',right=True)
        rc("axes", grid=False)
        a_func()
        
        from matplotlib.backends.backend_pdf import PdfPages
        pp= PdfPages(a_func.__name__+".pdf")
        fig = a_func()
        # plt.show()

        plt.savefig(pp, format='pdf',bbox_inches='tight')
        plt.clf()
        pp.close()
        

    return wrapTheFunction


@myplot
def my_sine():
    theta = np.array(np.linspace(0, 2 * np.pi, 100))
    y = np.sin(theta)
    
    fig = plt.plot(theta,y)
    # plt.show()
    return fig
    
my_sine()







