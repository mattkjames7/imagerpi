import numpy as np
import PyFileIO as pf
import os
from .. import Globals


def ReadDataIndex():
	'''
	Reads index file containing a list of all of the dates with their
	associated data file name (so that we can pick the version 
	automatically).
	'''
	fname = Globals.DataPath + 'index.dat'

	return ReadIndex(fname)



def ReadOrbitIndex():
	'''
	Reads index file containing a list of all of the dates with their
	associated data file name (so that we can pick the version 
	automatically).
	'''
	fname = Globals.DataPath + 'orbit.dat'

	return ReadIndex(fname)

def ReadIndex(fname):
	
	#define the dtype
	dtype = [('Date','int32'),('FileName','object'),('Version','int16')]
	
	
	#check it exists
	if not os.path.isfile(fname):
		return np.recarray(0,dtype=dtype)
		
	#read the index file
	try:
		data = pf.ReadASCIIData(fname,True,dtype=dtype)
	except:
		return np.recarray(0,dtype=dtype)
		
	return data
