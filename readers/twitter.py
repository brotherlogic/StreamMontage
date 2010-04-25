# Pulls out the details of your twitter feed
#
# Settings:
#  user: username
#  pwd : password

# Read the settings
lines = open('twitter.settings','r').readlines()
for line in lines:
    if line.startswith('user='):
        user = line.strip()[5:]
    elif line.startswith('pwd='):
        pwd = line.strip()[4:]


url = "http://api.twitter.com/1/statuses/friends_timeline"
