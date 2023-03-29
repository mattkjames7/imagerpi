import numpy as np
from .. import Globals
import os
import PyFileIO as pf
import re

#this is the base URL for the data
url0 = 'https://cdaweb.gsfc.nasa.gov/pub/data/image/rpi/rpi_Ne_fp_along_orbit/rpi_electron_density_CDF/'
urlo0 = 'https://cdaweb.gsfc.nasa.gov/pub/data/image/orbit/euv_orbit_cdf/'

def _ExtractCDFs(fname):
	'''
	read in the html and extract the cdf file names, dates and version numbers

	'''
	#read the file in
	lines = pf.ReadASCIIFile(fname)
	nl = lines.size

	#determine which lines contain a file name
	use = np.zeros(nl,dtype='bool')
	for i,l in enumerate(lines):
		if '.cdf"' in l and 'image_electron_density_' in l:
			use[i] = True
	keep = np.where(use)[0]
	lines = lines[keep]
	nl = lines.size

	#extract cdf names
	cdfs = np.zeros(nl,dtype='object')
	for i,l in enumerate(lines):
		s = l.split('"')
		cdfs[i] = s[1]


	
	#get dates
	dp = re.compile('\d\d\d\d\d\d\d\d')
	dates = np.zeros(nl,dtype='int32')
	for i in range(0,nl):
		dates[i] = np.int32(dp.search(cdfs[i]).group())
	
	#get versions
	vp = re.compile('v\d\d')
	vers = np.zeros(nl,dtype='int16')
	for i in range(0,nl):
		vers[i] = np.int16((vp.search(cdfs[i]).group()).replace('v',''))


	#get urls
	years = dates // 10000
	urls = np.zeros(nl,dtype='object')
	for i,c in enumerate(cdfs):
		urls[i] = url0 + '{:04d}/'.format(years[i]) + c

	return cdfs,urls,dates,vers

def _ExtractOrbitCDFs(fname):
	'''
	read in the html and extract the cdf file names, dates and version numbers

	'''
	#read the file in
	lines = pf.ReadASCIIFile(fname)
	nl = lines.size

	#determine which lines contain a file name
	use = np.zeros(nl,dtype='bool')
	for i,l in enumerate(lines):
		if '.cdf"' in l and 'image_or_euv_orbit_' in l:
			use[i] = True
	keep = np.where(use)[0]
	lines = lines[keep]
	nl = lines.size

	#extract cdf names
	cdfs = np.zeros(nl,dtype='object')
	for i,l in enumerate(lines):
		s = l.split('"')
		cdfs[i] = s[1]


	
	#get dates
	dp = re.compile('\d\d\d\d\d\d\d\d')
	dates = np.zeros(nl,dtype='int32')
	for i in range(0,nl):
		dates[i] = np.int32(dp.search(cdfs[i]).group())
	
	#get versions
	vp = re.compile('v\d\d')
	vers = np.zeros(nl,dtype='int16')
	for i in range(0,nl):
		vers[i] = np.int16((vp.search(cdfs[i]).group()).replace('v',''))


	#get urls
	years = dates // 10000
	urls = np.zeros(nl,dtype='object')
	for i,c in enumerate(cdfs):
		urls[i] = urlo0 + '{:04d}/'.format(years[i]) + c

	return cdfs,urls,dates,vers

def ListRepoFiles():
	'''
	List all of the files which can be downloaded.

	'''

	years = np.arange(2000,2006)

	#the temporary directory to store each html file in
	tmpdir = Globals.DataPath + 'tmp/'
	if not os.path.isdir(tmpdir):
		os.makedirs(tmpdir)

	#loop through each year, download the page and extract names/versions
	urls = np.array([],dtype='object')
	dates = np.array([],dtype='int32')
	vers = np.array([],dtype='int16')
	cdfs = np.array([],dtype='object')
	for y in years:
		tmpfile = tmpdir + '{:04d}'.format(y)
		url = url0 + '{:04d}'.format(y)
		os.system('wget --no-verbose {:s} -O {:s}'.format(url,tmpfile))
		c,u,d,v = _ExtractCDFs(tmpfile)

		urls = np.append(urls,u)
		cdfs = np.append(cdfs,c)
		dates = np.append(dates,d)
		vers = np.append(vers,v)

	return cdfs,urls,dates,vers



def ListOrbitFiles():
	'''
	List all of the files which can be downloaded.

	'''

	years = np.arange(2000,2006)

	#the temporary directory to store each html file in
	tmpdir = Globals.DataPath + 'tmp/'
	if not os.path.isdir(tmpdir):
		os.makedirs(tmpdir)

	#loop through each year, download the page and extract names/versions
	urls = np.array([],dtype='object')
	dates = np.array([],dtype='int32')
	vers = np.array([],dtype='int16')
	cdfs = np.array([],dtype='object')
	for y in years:
		tmpfile = tmpdir + '{:04d}'.format(y)
		url = urlo0 + '{:04d}'.format(y)
		os.system('wget --no-verbose {:s} -O {:s}'.format(url,tmpfile))
		c,u,d,v = _ExtractOrbitCDFs(tmpfile)

		urls = np.append(urls,u)
		cdfs = np.append(cdfs,c)
		dates = np.append(dates,d)
		vers = np.append(vers,v)

	return cdfs,urls,dates,vers

