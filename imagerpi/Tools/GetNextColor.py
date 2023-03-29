import numpy as np


def GetNextColor(ax,alpha=1.0):
	
	#get the color from the axes in hex
	hx = ax._get_lines.get_next_color()[1:]
	
	#convert to RGBA
	col = [int(hx[i*2:(i+1)*2],16)/255 for i in range(0,3)]
	col.append(alpha)
	
	return col
