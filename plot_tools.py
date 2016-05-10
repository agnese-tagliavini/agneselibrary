# ------------------------------------------------------------------------------------------------
#
# Contents: This library creates alternative personalized palettes for 3D object plots
#           for example VERTEX FUNCTIONS
#
#---------------------------------------------------------------------------------------------------

import numpy as np
import math
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as pl

#--------------------------------------Dictionary to define cmap---------------------------------------------

def create_palette_green():
    blue = [0,0,1.0] #RGB
    bluepos = 0.0
    green = [0,1.0,0]
    greenpos= 0.25
    white = [1.0,1.0,1.0]
    whitepos= 0.5
    yellow = [1.0,1.0,0]
    yellowpos = 0.75
    red = [1.0,0.0,0]
    redpos = 1.0
    cdict = {'red': ((bluepos,blue[0],blue[0]),
                    (greenpos,green[0],green[0]),
                    (whitepos,white[0],white[0]),
                    (yellowpos,yellow[0],yellow[0]),
                    (redpos,red[0],red[0])),
                    
             'green':((bluepos,blue[1],blue[1]),
                    (greenpos,green[1],green[1]),
                    (whitepos,white[1],white[1]),
                    (yellowpos,yellow[1],yellow[1]),
                    (redpos,red[1],red[1])),

             'blue': ((bluepos,blue[2],blue[2]),
                    (greenpos,green[2],green[2]),
                    (whitepos,white[2],white[2]),
                    (yellowpos,yellow[2],yellow[2]),
                    (redpos,red[2],red[2])),
                    
                    }
    return cdict

def create_palette_georg():
    grey = [0.27,0.27,0.27] #RGB
    greypos = 0.0
    darkblue = [0.16,0.30,1.0]
    darkbluepos= 0.14 
    lightblue = [0.25,1.0,1.0]
    lightbluepos = 0.30
    white = [1.0,1.0,1.0]
    whitepos= 0.5
    yellow = [1.0,1.0,0.20]
    yellowpos = 0.70
    red = [1.0,0.25,0.25]
    redpos = 0.86
    violet =[0.70,0.30,0.9]
    violetpos= 1.0
    cdict = {'red': ((greypos,grey[0],grey[0]),
                    (darkbluepos,darkblue[0],darkblue[0]),
                    (lightbluepos,lightblue[0],lightblue[0]),
                    (whitepos,white[0],white[0]),
                    (yellowpos,yellow[0],yellow[0]),
                    (redpos,red[0],red[0]),
                    (violetpos,violet[0],violet[0])),
                    
          'green': ((greypos,grey[1],grey[1]),
                    (darkbluepos,darkblue[1],darkblue[1]),
                    (lightbluepos,lightblue[1],lightblue[1]),
                    (whitepos,white[1],white[1]),
                    (yellowpos,yellow[1],yellow[1]),
                    (redpos,red[1],red[1]),
                    (violetpos,violet[1],violet[1])),

          'blue': ((greypos,grey[2],grey[2]),
                    (darkbluepos,darkblue[2],darkblue[2]),
                    (lightbluepos,lightblue[2],lightblue[2]),
                    (whitepos,white[2],white[2]),
                    (yellowpos,yellow[2],yellow[2]),
                    (redpos,red[2],red[2]),
                    (violetpos,violet[2],violet[2])),
                    }
    return cdict


def create_interactive_palette(x):
    cdict = {'red': ((x['color1'][0],x['color1'][1],x['color1'][1]),
                    (x['color2'][0],x['color2'][1],x['color2'][1]),
                    (x['color3'][0],x['color3'][1],x['color3'][1]),
                    (x['color4'][0],x['color4'][1],x['color4'][1]),
                    (x['color5'][0],x['color5'][1],x['color5'][1]),
                    (x['color6'][0],x['color6'][1],x['color6'][1]),
                    (x['color7'][0],x['color7'][1],x['color7'][1]),
                    (x['color8'][0],x['color8'][1],x['color8'][1]),
                    (x['color9'][0],x['color9'][1],x['color9'][1])),
                    
          'green': ((x['color1'][0],x['color1'][2],x['color1'][2]),
                    (x['color2'][0],x['color2'][2],x['color2'][2]),
                    (x['color3'][0],x['color3'][2],x['color3'][2]),
                    (x['color4'][0],x['color4'][2],x['color4'][2]),
                    (x['color5'][0],x['color5'][2],x['color5'][2]),
                    (x['color6'][0],x['color6'][2],x['color6'][2]),
                    (x['color7'][0],x['color7'][2],x['color7'][2]),
                    (x['color8'][0],x['color8'][2],x['color8'][2]),
                    (x['color9'][0],x['color9'][2],x['color9'][2])),

          'blue': ((x['color1'][0],x['color1'][3],x['color1'][3]),
                    (x['color2'][0],x['color2'][3],x['color2'][3]),
                    (x['color3'][0],x['color3'][3],x['color3'][3]),
                    (x['color4'][0],x['color4'][3],x['color4'][3]),
                    (x['color5'][0],x['color5'][3],x['color5'][3]),
                    (x['color6'][0],x['color6'][3],x['color6'][3]),
                    (x['color7'][0],x['color7'][3],x['color7'][3]),
                    (x['color8'][0],x['color8'][3],x['color8'][3]),
                    (x['color9'][0],x['color9'][3],x['color9'][3])),
                  }
    return cdict
