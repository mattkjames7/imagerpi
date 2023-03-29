import numpy as np
from ..Tools.ReadCDF import ReadCDF
from ..Downloading.ReadDataIndex import ReadOrbitIndex
from .. import Globals

def ReadOrbitCDF(Date,Quiet=False):
    
	# get the search path
	path = Globals.DataPath + 'orbit/'

	#get the data index
	idx = ReadOrbitIndex()

	#see if there are any files in the index which match
	match = np.where(Date == idx.Date)[0]
	if match.size == 0:
		if not Quiet:
			print('No data found on {:d}'.format(Date))
		return None,None

	#check for multiple versions
	if match.size > 1:
		I = idx.Version[match].argmax()
		fname = path + idx.FileName[I]
	else:
		fname = path + idx.FileName[match[0]]


	return ReadCDF(fname)
    