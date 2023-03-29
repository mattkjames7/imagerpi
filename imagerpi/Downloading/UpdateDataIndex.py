import os 
import PyFileIO as pf
from .. import Globals

def UpdateDataIndex(idx):
	'''
	Updates the data index file.
	
	Input:
		idx: numpy.recarray containing the file names.
	'''
	fname = Globals.DataPath + 'index.dat'
	pf.WriteASCIIData(fname,idx)


def UpdateOrbitIndex(idx):
	'''
	Updates the data index file.
	
	Input:
		idx: numpy.recarray containing the file names.
	'''
	fname = Globals.DataPath + 'orbit.dat'
	pf.WriteASCIIData(fname,idx)
