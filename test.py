from reddit import client
from reddit.user import User
from reddit.reddits import Subreddit

tim = client.login('timsbot')

print tim.link_karma()

tim.submit("test", "self", "Sent from bot", "123 Test")












#for c in range(0, len(k)):
#    print k[c].id()



