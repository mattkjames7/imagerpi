import numpy as np


def ReduceDownloadList(files,urls,Date,Ver,idx,Overwrite=False):
	'''
	'''
	
	nf = np.size(files)
	
	#get unique dates
	ud = np.unique(Date)
	
	keep = np.ones(nf,dtype='bool')
	#remove multiple versions
	for i in range(0,ud.size):
		use = np.where(Date == ud[i])[0]
		if use.size > 1:
			bad = np.where(Ver[use] < np.max(Ver[use]))[0]
			keep[use[bad]] = False
			
			
	#now remove versions which exist
	if not Overwrite:
		for i in range(0,nf):
			if keep[i]:
				inidx = ((idx.Date == Date[i]) & (idx.Version == Ver[i])).any()
				if inidx:
					keep[i] = False



	
	#reduce arrays
	use = np.where(keep)[0]
	
	urls = urls[use]
	files = files[use]
	Date = Date[use]
	Ver = Ver[use]
	
	return files,urls,Date,Ver
