image_dim = (2560,1024)

iconsize = 256

num_icons = (image_dim[0]/iconsize)*(image_dim[1]/iconsize)

import os
files = []
for f in os.listdir('downloads'):
    if f.endswith('square.jpg'):
        files.append('downloads/' + f)

from random import choice
while len(files) < num_icons:
    files.append(choice(files))

command = 'montage -geometry 256x256+0+0 -tile ' + `image_dim[0]/iconsize` + 'x' + `image_dim[1]/iconsize`

for file in files:
    command += " " + file

command += " " + "out.jpg"

os.popen(command).readlines()
