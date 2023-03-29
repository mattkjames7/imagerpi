import numpy as np
from . import Globals
import RecarrayTools as RT

def ReadDensity():
    
	fname = Globals.DataPath + 'Density.bin'
	return RT.ReadRecarray(fname)