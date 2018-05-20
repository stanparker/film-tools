# For hiding XML files from Sony Cameras


import os
import sys

if len(sys.argv) is not 2:
    print ("Improper number of arguments.")

else:
    parent = sys.argv[1]

    for root, dirs, files in os.walk(parent):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        if not files:
            continue

        prefix = os.path.basename(root)

        for f in files:
            if ".XML" in str(f):
                new_f = "." + str(f)
                print ("\n \n Renaming:")
                print ( os.path.join(root, f) + "\n" )
                print ("To:")
                print ( os.path.join(root, new_f))

                os.rename(os.path.join(root, f), os.path.join(root, new_f))
