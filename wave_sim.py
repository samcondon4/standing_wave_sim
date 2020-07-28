'''##########################################################
wave_sim:

    This script creates a standing wave simulator. It defines
    an incident wave traveling in a lengthwise constrained 
    medium as well as the resulting reflected wave. In the
    medium, the superposition of the incident wave and the
    the reflected wave create a standing wave. All three
    waves are displayed in individual subplots.

    A user can interact with this program by specifying parameters
    of the medium and the waves generated. These parameters are
    defined below:

        L: length of the medium (m.)
        r: reflection coefficient (unitless)
        v: phase velocity of wave (m./s.)
        f: frequency of the wave (Hz.)
    
    These parameters can be specified in two different ways.
    First, the user can run the python script and supply 
    the program with all four arguments respectively from the
    command line, or the values of L, r, v, and f can be manually
    changed and the program can be run by specifying no arguments.

    By default, in the combined wave plot, traces of previous wave
    states will be plotted in green while the current wave state
    is shown in red. A fifth parameter can be set to turn on/off
    this trace plot.

        plottrace: flag for tracing previous states of combined wave
    
    This argument can be specified as the one and only argument if values
    for L, r, v, and f are not specified at the command line, OR, if L, r, v, and f
    are specified then this parameter can be set with the 5th and final 
    command line argument.

Sam Condon
04/20/2020
###########################################################'''

#import needed packages
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as mpanimation 
import sys


'''#########################################################
WaveSystem:

    Object definition to hold all parameters of the simulation
    system and functions to generate plot values.
#########################################################'''
class WaveSystem:

    def __init__(self, L, r, v, f, resolution=200):
        self.L = L
        self.r = r
        self.v = v
        self.f = f
        self.resolution = resolution

        self.x = np.linspace(0,L,self.resolution)
        self.refx = 2*self.L - self.x
        self.incident = []
        self.reflected = []
        self.combined = []

    def update_incident(self, t):
        self.incident = -np.sin((2*np.pi*(self.f/self.v)*self.x) - (2*np.pi*self.f*t))

    def update_reflected(self, t):
        self.reflected = self.r*np.sin((2*np.pi*(self.f/self.v)*self.refx) - (2*np.pi*self.f*t))

    def update_combined(self):
        self.combined = np.add(self.incident,self.reflected)


#################################################################
'''############################################################
paramset():
    Function used to collect command line arguments and set the
    wave and medium parameters

    IF NOT RUNNING THIS SCRIPT WITH COMMAND LINE ARGUMENTS, THEN
    L, r, v, and f CAN BE MANUALLY CHANGED BELOW AND THE SCRIPT
    WILL RUN WITHOUT ANY COMMAND LINE ARGUMENTS. OTHERWISE, SPECIFY
    4 ARGUMENTS CORRESPONDING TO L, r, v, and f
############################################################'''
plottrace = 1
L = 1
r = 1
v = 1
f = 1

def paramset():
    global plottrace, L, r, v, f
    if(len(sys.argv) == 2):
        plottrace = int(sys.argv[1])

    elif(len(sys.argv) >= 5):
        L = float(sys.argv[1])
        r = float(sys.argv[2])
        v = float(sys.argv[3])
        f = float(sys.argv[4])
        if(len(sys.argv) == 6):
            plottrace = int(sys.argv[5])
#################################################################



paramset() #set WaveSystem input parameters

W = WaveSystem(L,r,v,f) #create WaveSystem instance

#Create figure and subplots
fig = plt.figure()
incident = plt.subplot2grid((3,1), (0,0))
reflected = plt.subplot2grid((3,1), (1,0))
combined = plt.subplot2grid((3,1), (2,0))

#Set x and y limits for subplots
incident.set_xlim(0,L)
reflected.set_xlim(0,L)
combined.set_xlim(0,L)

incident.set_ylim(-2,2)
reflected.set_ylim(-2,2)
combined.set_ylim(-3,3)

#Grab plot object to update values later on
lineinc, = incident.plot([],[])
lineref, = reflected.plot([],[])
linecomb, = combined.plot([],[])

#Set plot titles
iwavetext = incident.text(0.02, 0.9, 'Incident Wave', transform=incident.transAxes)
rwavetext = reflected.text(0.02, 0.9, 'Reflected Wave', transform=reflected.transAxes)
cwavetext = combined.text(0.02, 0.9, 'Combined Wave', transform=combined.transAxes)

#Initialize time text that will show the current time in seconds
timetext = incident.text(0.02, 0.8, '', transform=incident.transAxes)

#Animation function. Called every
def animate(i):
    W.update_incident(i*0.01)    #generate new values for incident wave plot
    W.update_reflected(i*0.01)   #generate new values for reflected wave plot
    W.update_combined()          #generate new values for combined wave plot
    timetext.set_text("t = %.2f" % (i*0.01)) #update time text value
    lineinc.set_data(W.x, W.incident)
    lineref.set_data(W.x, W.reflected)

    #Trace old values of combined wave
    if(i*0.01 < (1/W.f) and plottrace > 0):
        combined.plot(W.x,W.combined, color='green', linewidth=0.25)
   

    linecomb.set_data(W.x, W.combined)
    linecomb.set_linewidth(3)
    linecomb.set_color('red')
    return lineinc, lineref,

#Create the animation, setting blit to True should make the animation run faster but that breaks everything...
anim = mpanimation.FuncAnimation(fig, animate, frames=1000, interval=20, blit=False)

plt.show()
