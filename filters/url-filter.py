import urllib2
import re
import sys

def getUrl(url):
    try:
        var = urllib2.urlopen(url)
    except:
        return ""
    return var.geturl()

def processTwitPic(url):
    tmatcher = re.compile('id="photo-display" src="(http.*)"')
    for line in urllib2.urlopen(url):
        for match in tmatcher.findall(line):
            return match
    return None

def processFlickr(url):    
    fmatcher = re.compile('(http.*farm.*jpg)')
    for line in urllib2.urlopen(url):
        for match in fmatcher.findall(line):
            return match

    return None


def resolveUrl(url):
    act_url = getUrl(url)

    if act_url.startswith('http://www.flickr.com/'):
        return processFlickr(url)
    elif act_url.startswith('http://twitpic.com'):
        return processTwitPic(url)


url_matcher = re.compile('(http:.*)\s*')
for match in url_matcher.findall(sys.argv[1]):
    m = resolveUrl(match)
    if m != None:
        print m
