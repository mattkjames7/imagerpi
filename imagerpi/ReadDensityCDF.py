import numpy as np
from .Downloading.ReadDataIndex import ReadDataIndex
from . import Globals
from .Tools.ReadCDF import ReadCDF

def ReadDensityCDF(date):
    
	idx = ReadDataIndex()

	use = np.where(idx.Date == date)[0]
	if use.size == 0:
		return None
	
	idx = idx[use]
	ind = idx.Version.argmax()

	fname = Globals.DataPath + 'cdf/' + idx.FileName[ind]

	return ReadCDF(fname)