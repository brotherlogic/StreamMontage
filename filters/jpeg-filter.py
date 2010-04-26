import re,sys

matcher = re.compile('(http.*?jpe?g)')

def filter(line):
    matches = matcher.findall(line)
    return matches

for match in filter(sys.argv[1]):
    print match.strip()
