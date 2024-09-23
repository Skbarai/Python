#argv is like list with argument values from user here we put pyhton file name at argv[0] and some argument
import sys
if len(sys.argv)==2:
    print(f"Hello {sys.argv[1]} ")