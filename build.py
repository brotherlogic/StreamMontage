import os,re

smatch = re.compile('\s(\d*x\d*)\s')

def read_filters():
    filters = []
    for line in os.listdir('filters'):
        if line.endswith('py'):
            filters.append(line.strip())
    return filters

filters = read_filters()

# 1 - download all the images
allfiles = []
for reader in os.listdir('readers'):
    if reader.endswith('.py'):
        lines = os.popen('python readers/' + reader)
    
        for line in lines:
            for filter in filters:
                results = os.popen('python filters/' + filter + ' "' + line + '"').readlines()
                for res in results:
                    allfiles.append(res.strip())


for f in allfiles:
    os.popen('wget -c ' + f + ' -P downloads/').readlines()

for f in os.listdir('downloads/'):
    if not f.endswith('square.jpg'):
        for match in smatch.findall(os.popen('identify downloads/' + f).readlines()[0]):

            (x,y) = match.split('x')
            
            maxd = 0
            if int(x) > int(y):
                maxd = int(y)
            else:
                maxd = int(x)


            os.popen('convert -gravity Center -crop ' + `maxd` + 'x' + `maxd` + '+0+0 -resize 256x256 downloads/' + f + ' downloads/' + f + '.square.jpg').readlines()
    

os.popen('python make_image.py').readlines()
