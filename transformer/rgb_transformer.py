import numpy as np
import os
import matplotlib.pyplot as plt

def convert_to_bnw(origin_path, storage_path=""):
	if os.path.exists(origin_path):
		origin = plt.imread(origin_path)
		bnw = origin[:,:,0]
		origin_name, origin_ext = origin_path.split("/")[-1].split(".")
		plt.imsave(storage_path + "/__" + origin_name + "." + origin_ext, bnw)
		return "__" + origin_name + "." + origin_ext
	return ""
		
