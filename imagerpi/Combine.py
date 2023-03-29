import numpy as np
from .Downloading.ReadDataIndex import ReadDataIndex
from .ReadDensityCDF import ReadDensityCDF
import DateTimeTools as TT
from . import Globals
import RecarrayTools as RT

def _getCDF(date):

	cdf,_ = ReadDensityCDF(date)

	dtype = [	('Date','int32'),
	  			('ut','float32'),
				('utc','float64'),
				('Density','float64')]
	data = np.recarray(cdf['Epoch'].size,dtype=dtype)
	data.Date,data.ut = TT.CDFEpochtoDate(cdf['Epoch'])
	data.utc = TT.ContUT(data.Date,data.ut)
	data.Density = cdf['den']

	return data

def Combine():
    
	idx = ReadDataIndex()

	dates = idx.Date
	dates.sort()

	nd = dates.size

	cdfs = []
	lens = []
	for i in range(0,nd):
		print('\rReading {:d} of {:d}'.format(i+1,nd),end='')
		cdf = _getCDF(dates[i])
		cdfs.append(cdf)
		lens.append(cdf.size)
	print()

	n = np.sum(lens)


	data = np.recarray(n,dtype=cdfs[0].dtype)

	p = 0
	for i in range(0,nd):
		print('\rCombining {:d} of {:d}'.format(i+1,nd),end='')
		data[p:p+lens[i]] = cdfs[i]
		p += lens[i]
	print()

	srt = np.argsort(data.utc)
	data = data[srt]

	fname = Globals.DataPath + 'Density.bin'
	RT.SaveRecarray(data,fname,StoreDtype=True)