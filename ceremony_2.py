import os
import sys

if len(sys.argv) < 2:
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

            print ("\n \n Renaming:")
            print ( os.path.join(root, f) + "\n" )
            print ("To:")
            new_name = str.replace(os.path.join(root, f),"2018-03-18 Ceremony at the Village", "2018-03-18 Ceremony at the Village 2")
            print ( new_name )


            if "--dry" not in sys.argv:
                print ("not a dry run")
                os.rename(os.path.join(root, f), new_name)
