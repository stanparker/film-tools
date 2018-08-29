# For hiding XML files from Sony Cameras
# Takes two argument: the root folder to perform the operation on and the destination to copy to

import os
import sys
from shutil import copyfile


if len(sys.argv) is not 3:
    print ("Improper number of arguments.")

else:
    parent = sys.argv[1]
    new_root = sys.argv[2]

    for root, dirs, files in os.walk(parent):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']

        if not files:
            continue

        prefix = os.path.basename(root)

        for f in files:
            if ".wav" in str(f).lower() or ".mp3" in str(f).lower():

                print ("\n \n Attempting to copy:")
                print ( os.path.join(root, f) + "\n" )

                try:
                    copyfile(os.path.join(root, f), os.path.join(new_root, f))
                    print ("Success. \n \n")

                except:
                    print ("Failed. \n \n")
