image_dim = [2560,1024]

for line in open('image.settings').readlines():
    if line.startswith('height'):
        image_dim[1] = int(line.strip()[7:])
    elif line.startswith('width'):
        image_dim[0] = int(line.strip()[6:])

iconsize = 128

num_icons = (image_dim[0]/iconsize)*(image_dim[1]/iconsize)

import os
files = []
for f in os.listdir('downloads'):
    if f.endswith('square.jpg'):
        files.append('downloads/' + f)

from random import choice
while len(files) < num_icons:
    files.append(choice(files))

command = 'montage -geometry 128x128+0+0 -tile ' + `image_dim[0]/iconsize` + 'x' + `image_dim[1]/iconsize`

for file in files:
    command += ' "' + file + '"'

command += " " + "out.jpg"

os.popen(command).readlines()
