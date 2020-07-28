wave:

    Class defining a wave system. Can be used in a standing wave simulation.

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

