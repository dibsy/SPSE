import glob
import os

for item in glob.glob(os.path.join(".","*.py")):
	print item
