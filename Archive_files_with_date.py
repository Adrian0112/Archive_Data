

import os
from pathlib import Path
import shutil
import sys
from datetime import date
import glob

today = str(date.today())

os.chdir('C:/Users/PLADREB1/Desktop/InProgress/script_transfer')


print(os.getcwd())
#Path(today + "_old").mkdir(exist_ok=True)

for i in range (10):

    if not os.path.exists(today + "_old"):
      os.mkdir(today + "_old")


    for file in os.listdir():
     if file == '._old':
         continue

    shutil.move(file, today + "_old")
