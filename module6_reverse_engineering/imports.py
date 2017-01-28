import pefile
import sys

filename = sys.argv[1]
dll_name = sys.argv[2]

pe = pefile.PE(filename)

for item in pe.DIRECTORY_ENTRY_IMPORT:
    if item.dll.lower() == dll_name.lower() :
        print item.dll.lower()
        for import_fn in item.imports:
            print hex(import_fn.address), import_fn.name


            
