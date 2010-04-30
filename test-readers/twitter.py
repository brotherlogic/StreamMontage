# Pulls out the details of your twitter feed
#
# Settings:
#  user: username
#  pwd : password

import os

# Read the settings
lines = open('twitter.settings','r').readlines()
for line in lines:
    if line.startswith('user='):
        user = line.strip()[5:]
    elif line.startswith('pwd='):
        pwd = line.strip()[4:]


url = "http://api.twitter.com/1/statuses/friends_timeline.xml?count=200"

#Hack for now - use curl to pull the timeline
for line in os.popen('curl -s -u ' + user + ':' + pwd + ' ' + url).readlines():
    if line.strip().startswith('<text>'):
        print line.strip()[6:-7]
