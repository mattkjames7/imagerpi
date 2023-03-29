import numpy as np
from .ReadOrbitCDF import ReadOrbitCDF
import DateTimeTools as TT
from ..Downloading.ReadDataIndex import ReadOrbitIndex
from .. import Globals
import RecarrayTools as RT

def _ConvertOrbit(Date):
    
	dtype = [	('Date','int32'),
	  			('ut','float64'),
				('utc','float64'),
				('xgse','float64'),
				('ygse','float64'),
				('zgse','float64'),
				('xgsm','float64'),
				('ygsm','float64'),
				('zgsm','float64')]
	
	data,meta = ReadOrbitCDF(Date)

	n = data['Epoch'].size
	out = np.recarray(n,dtype=dtype)

	out.Date,out.ut = TT.CDFEpochtoDate(data['Epoch'])
	out.utc = TT.ContUT(out.Date,out.ut)

	out.xgse = data['GSE_POS'][:,0]
	out.ygse = data['GSE_POS'][:,1]
	out.zgse = data['GSE_POS'][:,2]

	out.xgsm = data['GSM_POS'][:,0]
	out.ygsm = data['GSM_POS'][:,1]
	out.zgsm = data['GSM_POS'][:,2]

	r = np.sqrt(out.xgsm**2 + out.ygsm**2 + out.zgsm**2)

	return out

def Convert():

	idx = ReadOrbitIndex()
	n = idx.size
	dates = idx.Date
	dates.sort()

	data = []
	c = 0
	for i in range(0,n):
		print('\rConvert Date {:08d} ({:04d} of {:04d})'.format(dates[i],i+1,n),end='')
		tmp = _ConvertOrbit(dates[i])
		data.append(tmp)
		c += tmp.size

	out = np.recarray(c,dtype=tmp.dtype)
	p = 0
	for i in range(0,n):
		print('\rFilling Date {:08d} ({:04d} of {:04d})'.format(dates[i],i+1,n),end='')
		out[p:p+data[i].size] = data[i]
		p += data[i].size
	print()
	fname = Globals.DataPath + 'Orbit.bin'
	RT.SaveRecarray(out,fname,StoreDtype=True)
