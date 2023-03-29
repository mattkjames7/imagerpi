from .. import Globals
import numpy as np
import os
from .ReadDataIndex import ReadDataIndex,ReadOrbitIndex
from .UpdateDataIndex import UpdateDataIndex,UpdateOrbitIndex
import RecarrayTools as RT
from .ReduceDownloadList import ReduceDownloadList
from .ListRepoFiles import ListRepoFiles,ListOrbitFiles

def DownloadData(Overwrite=False,Progress=False):
	'''
	Downloads EUV data

	Inputs
	======
	Overwrite : bool
		If True then existing files will be overwritten
	Progress : bool
		If True then download progress will be output by wget
	'''


	
	#create output path if it doesn't exist
	outpath = Globals.DataPath + 'cdf/'
	if not os.path.isdir(outpath):
		os.system('mkdir -pv '+outpath)


	#get a list of the files which we can download
	cdfs,urls,dates,vers = ListRepoFiles()

	#get the current index
	idx = ReadDataIndex()

	#reduce the list
	cdfs,urls,dates,vers = ReduceDownloadList(cdfs,urls,dates,vers,idx,Overwrite=Overwrite)

		
	#loop through each remaining date and start downloading
	nu = np.size(urls)
		
	if nu > 0:
		new_idx = np.recarray(nu,dtype=idx.dtype)
		new_idx.Date[:] = -1


		p = 0
		for j in range(0,nu):
			print('Downloading file {0} of {1} ({2})'.format(j+1,nu,cdfs[j]))

			if Progress:
				os.system('wget '+urls[j]+' -O '+outpath+cdfs[j])
			else:
				os.system('wget --no-verbose '+urls[j]+' -O '+outpath+cdfs[j])

			new_idx.Date[p] = dates[j]
			new_idx.FileName[p] = cdfs[j]
			new_idx.Version[p] = vers[j]
			p+=1
					
		new_idx = new_idx[:p]
			
			
		#check for duplicates within old index
		usen = np.ones(p,dtype='bool')
		useo = np.ones(idx.size,dtype='bool')
			
		for j in range(0,p):
			match = np.where(idx.Date == new_idx.Date[j])[0]
			if match.size > 0:
				if idx.Version[match[0]] > new_idx.Version[j]:
					#old one is newer (unlikely)
					usen[j] = False
				else:
					#new one is newer
					useo[match[0]] = False
		usen = np.where(usen)[0]
		new_idx = new_idx[usen]
		useo = np.where(useo)[0]
		idx = idx[useo]					
			
		#join indices together and update file
		idx_out = RT.JoinRecarray(idx,new_idx)
		srt = np.argsort(idx_out.Date)
		idx_out = idx_out[srt]
		UpdateDataIndex(idx_out)
			
			

def DownloadOrbit(Overwrite=False,Progress=False):
	'''
	Downloads Orbit

	Inputs
	======
	Overwrite : bool
		If True then existing files will be overwritten
	Progress : bool
		If True then download progress will be output by wget
	'''


	
	#create output path if it doesn't exist
	outpath = Globals.DataPath + 'orbit/'
	if not os.path.isdir(outpath):
		os.system('mkdir -pv '+outpath)


	#get a list of the files which we can download
	cdfs,urls,dates,vers = ListOrbitFiles()

	#get the current index
	idx = ReadOrbitIndex()

	#reduce the list
	cdfs,urls,dates,vers = ReduceDownloadList(cdfs,urls,dates,vers,idx,Overwrite=Overwrite)

		
	#loop through each remaining date and start downloading
	nu = np.size(urls)
		
	if nu > 0:
		new_idx = np.recarray(nu,dtype=idx.dtype)
		new_idx.Date[:] = -1


		p = 0
		for j in range(0,nu):
			print('Downloading file {0} of {1} ({2})'.format(j+1,nu,cdfs[j]))

			if Progress:
				os.system('wget '+urls[j]+' -O '+outpath+cdfs[j])
			else:
				os.system('wget --no-verbose '+urls[j]+' -O '+outpath+cdfs[j])

			new_idx.Date[p] = dates[j]
			new_idx.FileName[p] = cdfs[j]
			new_idx.Version[p] = vers[j]
			p+=1
					
		new_idx = new_idx[:p]
			
			
		#check for duplicates within old index
		usen = np.ones(p,dtype='bool')
		useo = np.ones(idx.size,dtype='bool')
			
		for j in range(0,p):
			match = np.where(idx.Date == new_idx.Date[j])[0]
			if match.size > 0:
				if idx.Version[match[0]] > new_idx.Version[j]:
					#old one is newer (unlikely)
					usen[j] = False
				else:
					#new one is newer
					useo[match[0]] = False
		usen = np.where(usen)[0]
		new_idx = new_idx[usen]
		useo = np.where(useo)[0]
		idx = idx[useo]					
			
		#join indices together and update file
		idx_out = RT.JoinRecarray(idx,new_idx)
		srt = np.argsort(idx_out.Date)
		idx_out = idx_out[srt]
		UpdateOrbitIndex(idx_out)
			
			
