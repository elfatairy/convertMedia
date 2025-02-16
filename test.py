import subprocess
import os
import shutil

path = "C:\\test\\slasel\\013-mkate3\\015.mp3".replace('\\', '/')
folder = "C:\\testMP3\\slasel\\013-mkate3/".replace('\\', '/')

shutil.copy(path, folder)

#print(f"{path} ==> {folder}")
#command = ['copy', path, folder]
#result = subprocess.run(command, capture_output=False, text=False, check=False)