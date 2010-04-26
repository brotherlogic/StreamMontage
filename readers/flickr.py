import os,re

matcher = re.compile('<link.*?href=\"(.*?)\"')

user = open('flickr.settings','r').readlines()[0].split('=')[1]

for line in os.popen('curl -s http://api.flickr.com/services/feeds/photos_friends.gne?user_id='+user+'&friends=0&display_all=1&lang=en-us&format=rss_200').readlines():
    for match in matcher.findall(line):
        print match
