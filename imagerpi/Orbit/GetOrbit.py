import numpy as np
import RecarrayTools as RT
from .. import Globals

def GetOrbit():
    
	if Globals.orbit is None:
		fname = Globals.DataPath + 'Orbit.bin'
		Globals.orbit = RT.ReadRecarray(fname)
	
	return Globals.orbit