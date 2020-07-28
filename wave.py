import numpy as np
import matplotlib.pyplot as plot

'''##################################################################################
WaveSystem:
    
    This class defines a wave system in which a medium lenght L,
    reflection coefficient r, phase velocity v, and wave frequency f
    can be defined and plotted if desired. The other arguments fig
    and axes are matplotlib objects used for plotting the incident and
    reflected waves as well as their superposition.

###################################################################################'''

class WaveSystem:

    def __init__(self, L, r, v, f, fig=None, axes=None, resolution=10000):
        self.L = L
        self.r = r
        self.v = v
        self.f = f
        self.fig = fig
        self.resolution = resolution

        self.x = np.linspace(0,L,self.resolution)
       
        if(len(axes) == 3):

            for k in axes:
                k.set_xlim(0,L)
                k.set_ylim(-1,1)

            self.incidentplot = axes[0]
            self.incidentdata, = self.incidentplot.plot([], []) 

            self.reflectedplot = axes[1]
            self.reflecteddata, = self.reflectedplot.plot([], [])
            
            self.superpositionplot = axes[2]
            self.superposdata, = self.superpositionplot.plot([], [])



    '''##########################################
    show_reflected():
        Plot the reflected wave at time t
    ##########################################'''


    '''##########################################
    show_incident():
        Plot the incident wave at time t
    ###########################################'''
    def show_incident(self, t):
        incident = np.cos((2*np.pi*(self.f/self.v)*self.x) - (2*np.pi*self.f*t))
        self.incidentdata.set_data(self.x, incident)
        self.incidentplot.text((3/4)*self.L,(3/4)*self.L,str(t))

