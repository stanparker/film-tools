import os
from glob import glob
import subprocess
import re
import csv

PATH = "/Volumes/StevieNicks/"

results = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.MP4'))]
results.extend ([y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.MOV'))])
results.extend ([y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.mp4'))])
results.extend ([y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.mov'))])

file = open ("results-2.csv","w")

for source_file in results:


    command = 'mediainfo --Inform="General;%Duration/String3%" "' + source_file + '"'
    duration = subprocess.check_output(command, shell=True)

    print source_file
    print duration

    file.write(result + ", " + duration)

file.close()
