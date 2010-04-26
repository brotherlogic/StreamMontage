import os,pkgutil,filters

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

    lines = ['Hello','Goodbye','http://donkey.jpeg']
    
    for line in lines:
        for filter in filters:
            results = os.popen('python filters/' + filter + ' "' + line + '"').readlines()
            for res in results:
                allfiles.append(res.strip())


print allfiles
    

