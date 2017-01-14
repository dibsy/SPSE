# Take a DLL name as input and check if a given PE imports it and print the list of imports

import pefile
pe = pefile.PE("xyz.dll")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
	print entry.dll
	for imp in entry.imports:
		print "\t",imp.name
